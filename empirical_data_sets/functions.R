library(ape)
library(TreeSim)
library(phangorn)
library(NELSI)

####################
# Cut terminal branches sampling within a date span
cut_term_branches <- function(tr_chrono, span_cut = 1:10){
  term_branches <- (1:nrow(tr_chrono$edge))[tr_chrono$edge[, 2] %in% 1:length(tr_chrono$tip.label)]
  term_branches <- sample(term_branches, (length(term_branches) - 1))
  tr_chrono$edge.length[term_branches] <- tr_chrono$edge.length[term_branches] / sample(span_cut, length(term_branches), replace = T)
  return(tr_chrono)
}


####################
# Simulate a heterochronous treee
get_tree_cal <- function(span_cut = c(1, 1.1), max_cal = 5, min_cal = 4, tr_time = 100, n_tax = 20, print_trees = T){

  if(max_cal >= tr_time || min_cal >= tr_time) stop('The calibration cannot be older than the tree')	     

  cal_time <- 0

  cal_stats <- vector()

  while(cal_time > max_cal || cal_time < min_cal){
    tr_temp <- sim.bd.taxa.age(n = n_tax, numbsim = 1, lambda = 1, mu = 0.5, age = tr_time)[[1]] 
    tr_cut <- cut_term_branches(tr_temp, span_cut = span_cut)

    tr_cut$edge.length <- tr_cut$edge.length * (tr_time / max(allnode.times(tr_cut)))
    cal_time <- max(allnode.times(tr_cut, tipsonly = T)) - min(allnode.times(tr_cut, tipsonly = T))

    if(print_trees){
      print(paste('current cal time is:' , cal_time))
      plot(tr_temp, edge.col = 'white', edge.width = 3)
      plot(tr_cut, edge.col = 'white', edge.width = 3)
      times_cut <- allnode.times(tr_cut)
      nodelabels(round(times_cut[(length(tr_cut$tip.label) + 1):length(times_cut)], 2))
      tiplabels(round(times_cut[1:length(tr_cut$tip.label)], 2))
    }
    cal_stats <- c(cal_stats, cal_time)
  }

  tr_cut$tip.label <- paste0(tr_cut$tip.label, '_', round(allnode.times(tr_cut, tipsonly = T), 2))
  
  return(list(chronogram = tr_cut, sim_stats = cal_stats))
}


#####################
# Function to make the xml file
##
make_xml_file <- function(seq_data, file_name, random_dates = F){

block1 <- "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><beast beautitemplate='Standard' beautistatus='' namespace=\"beast.core:beast.evolution.alignment:beast.evolution.tree.coalescent:beast.core.util:beast.evolution.nuc:beast.evolution.operators:beast.evolution.sitemodel:beast.evolution.substitutionmodel:beast.evolution.likelihood\" version=\"2.0\">\n    <data \n id=\"FILENAME\" \n name=\"alignment\">"

taxon_template <- "<sequence id=\"seq_TAXON_NAME\" taxon=\"TAXON_NAME\" totalcount=\"4\" value=\"SEQ_DATA\"/>"

###########################
taxon_block <- vector()
for(i in 1:nrow(seq_data)){
      taxon_block[i] <- gsub( 'TAXON_NAME', rownames(seq_data)[i], taxon_template)
      taxon_block[i] <- gsub('SEQ_DATA', paste0(as.character(seq_data[i,]), collapse = ''), taxon_block[i])
}
taxon_block <- paste(taxon_block, collapse = '\n')
#print(taxon_block)
###########################

block2 <- "</data>    \n <map name=\"Beta\">beast.math.distributions.Beta</map> \n <map name=\"Exponential\">beast.math.distributions.Exponential</map> \n <map name=\"InverseGamma\">beast.math.distributions.InverseGamma</map> \n <map name=\"LogNormal\">beast.math.distributions.LogNormalDistributionModel</map> \n <map name=\"Gamma\">beast.math.distributions.Gamma</map> \n  <map name=\"Uniform\">beast.math.distributions.Uniform</map> \n <map name=\"prior\">beast.math.distributions.Prior</map> \n <map name=\"LaplaceDistribution\">beast.math.distributions.LaplaceDistribution</map> \n <map name=\"OneOnX\">beast.math.distributions.OneOnX</map> \n <map name=\"Normal\">beast.math.distributions.Normal</map> \n"

block3 <- "<run chainLength=\"50000000\" id=\"mcmc\" spec=\"MCMC\"> \n     <state id=\"state\" storeEvery=\"5000\"> \n        <tree id=\"Tree.t:FILENAME\" name=\"stateNode\"> \n   <trait id=\"dateTrait.t:FILENAME\" spec=\"beast.evolution.tree.TraitSet\" traitname=\"date-backward\">"

################################
date_template <- 'TAXON_NAME=DATE'
date_block <- vector()
tax_names <- rownames(seq_data)

tax_dates <- gsub('^.+_', '', tax_names)
if(random_dates){
	tax_dates <- sample(tax_dates)
}

for(i in 1:nrow(seq_data)){
      date_block[i] <- gsub('TAXON_NAME', tax_names[i], date_template)
      date_block[i] <- gsub('DATE',    tax_dates[i] , date_block[i] )
}
date_block <- paste(date_block, collapse = ',\n')
#print(date_block)

# BUT REMOVE LAST COLON
##############################

block4 <-  "<taxa id=\"TaxonSet.FILENAME\" spec=\"TaxonSet\"> \n      <data \n idref=\"FILENAME\" \n name=\"alignment\"/> \n  </taxa>   \n </trait> \n <taxonset idref=\"TaxonSet.FILENAME\"/>  \n  </tree> \n  <parameter id=\"ucldMean.c:FILENAME\" name=\"stateNode\">1.0</parameter> \n        <parameter id=\"ucldStdev.c:FILENAME\" lower=\"0.0\" name=\"stateNode\" upper=\"5.0\">0.5</parameter> \n   <stateNode dimension=\"98\" id=\"rateCategories.c:FILENAME\" spec=\"parameter.IntegerParameter\">1</stateNode> \n    <parameter id=\"popSize.t:FILENAME\" name=\"stateNode\">0.3</parameter>\n    </state>"

block5 <- "    <init estimate=\"false\" id=\"RandomTree.t:FILENAME\" initial=\"@Tree.t:FILENAME\" spec=\"beast.evolution.tree.RandomTree\" taxa=\"@FILENAME\"> \n
        <populationModel id=\"ConstantPopulation0.t:FILENAME\" spec=\"ConstantPopulation\"> \n
            <parameter id=\"randomPopSize.t:FILENAME\" name=\"popSize\">1.0</parameter> \n
        </populationModel> \n
    </init> \n
    <distribution id=\"posterior\" spec=\"util.CompoundDistribution\"> \n
        <distribution id=\"prior\" spec=\"util.CompoundDistribution\"> \n
            <distribution id=\"CoalescentConstant.t:FILENAME\" spec=\"Coalescent\"> \n
                <populationModel id=\"ConstantPopulation.t:FILENAME\" popSize=\"@popSize.t:FILENAME\" spec=\"ConstantPopulation\"/> \n
                <treeIntervals id=\"TreeIntervals.t:FILENAME\" spec=\"TreeIntervals\" tree=\"@Tree.t:FILENAME\"/> \n
            </distribution> \n
            <prior id=\"PopSizePrior.t:FILENAME\" name=\"distribution\" x=\"@popSize.t:FILENAME\"> \n
                <OneOnX id=\"OneOnX.0\" name=\"distr\"/> \n
            </prior> \n
            <prior id=\"MeanRatePrior.c:FILENAME\" name=\"distribution\" x=\"@ucldMean.c:FILENAME\"> \n
                <Uniform id=\"Uniform.0\" name=\"distr\" upper=\"Infinity\"/> \n
            </prior> \n
            <prior id=\"ucldStdevPrior.c:FILENAME\" name=\"distribution\" x=\"@ucldStdev.c:FILENAME\"> \n
                <Exponential id=\"Exponential.0\" name=\"distr\"> \n
                    <parameter estimate=\"false\" id=\"RealParameter.0\" name=\"mean\">0.3333</parameter> \n
                </Exponential> \n
            </prior> \n
        </distribution> \n
        <distribution id=\"likelihood\" spec=\"util.CompoundDistribution\"> \n
            <distribution data=\"@FILENAME\" id=\"treeLikelihood.FILENAME\" spec=\"TreeLikelihood\" tree=\"@Tree.t:FILENAME\"> \n
                <siteModel id=\"SiteModel.s:FILENAME\" spec=\"SiteModel\"> \n
                    <parameter estimate=\"false\" id=\"mutationRate.s:FILENAME\" name=\"mutationRate\">1.0</parameter> \n
                    <parameter estimate=\"false\" id=\"gammaShape.s:FILENAME\" name=\"shape\">1.0</parameter> \n
                    <parameter estimate=\"false\" id=\"proportionInvariant.s:FILENAME\" lower=\"0.0\" name=\"proportionInvariant\" upper=\"1.0\">0.0</parameter> \n
                    <substModel id=\"JC69.s:FILENAME\" spec=\"JukesCantor\"/> \n
                </siteModel> \n
                <branchRateModel clock.rate=\"@ucldMean.c:FILENAME\" id=\"RelaxedClock.c:FILENAME\" rateCategories=\"@rateCategories.c:FILENAME\" spec=\"beast.evolution.branchratemodel.UCRelaxedClockModel\" tree=\"@Tree.t:FILENAME\"> \n
                    <LogNormal S=\"@ucldStdev.c:FILENAME\" id=\"LogNormalDistributionModel.c:FILENAME\" meanInRealSpace=\"true\" name=\"distr\"> \n
                        <parameter estimate=\"false\" id=\"RealParameter.01\" lower=\"0.0\" name=\"M\" upper=\"1.0\">1.0</parameter> \n
                    </LogNormal> \n
                </branchRateModel> \n
            </distribution> \n
        </distribution> \n
    </distribution> \n
"

block6 <- "    <operator id=\"treeScaler.t:FILENAME\" scaleFactor=\"0.5\" spec=\"ScaleOperator\" tree=\"@Tree.t:FILENAME\" weight=\"3.0\"/>
    <operator id=\"treeRootScaler.t:FILENAME\" rootOnly=\"true\" scaleFactor=\"0.5\" spec=\"ScaleOperator\" tree=\"@Tree.t:FILENAME\" weight=\"3.0\"/>
    <operator id=\"UniformOperator.t:FILENAME\" spec=\"Uniform\" tree=\"@Tree.t:FILENAME\" weight=\"30.0\"/>
    <operator id=\"SubtreeSlide.t:FILENAME\" spec=\"SubtreeSlide\" tree=\"@Tree.t:FILENAME\" weight=\"15.0\"/>
    <operator id=\"narrow.t:FILENAME\" spec=\"Exchange\" tree=\"@Tree.t:FILENAME\" weight=\"15.0\"/>
    <operator id=\"wide.t:FILENAME\" isNarrow=\"false\" spec=\"Exchange\" tree=\"@Tree.t:FILENAME\" weight=\"3.0\"/>
    <operator id=\"WilsonBalding.t:FILENAME\" spec=\"WilsonBalding\" tree=\"@Tree.t:FILENAME\" weight=\"3.0\"/>
    <operator id=\"ucldMeanScaler.c:FILENAME\" parameter=\"@ucldMean.c:FILENAME\" scaleFactor=\"0.5\" spec=\"ScaleOperator\" weight=\"1.0\"/>
    <operator id=\"ucldStdevScaler.c:FILENAME\" parameter=\"@ucldStdev.c:FILENAME\" scaleFactor=\"0.5\" spec=\"ScaleOperator\" weight=\"3.0\"/>
    <operator id=\"CategoriesRandomWalk.c:FILENAME\" parameter=\"@rateCategories.c:FILENAME\" spec=\"IntRandomWalkOperator\" weight=\"10.0\" windowSize=\"1\"/>
    <operator id=\"CategoriesSwapOperator.c:FILENAME\" intparameter=\"@rateCategories.c:FILENAME\" spec=\"SwapOperator\" weight=\"10.0\"/>
    <operator id=\"CategoriesUniform.c:FILENAME\" parameter=\"@rateCategories.c:FILENAME\" spec=\"UniformOperator\" weight=\"10.0\"/>
    <operator id=\"relaxedUpDownOperator.c:FILENAME\" scaleFactor=\"0.75\" spec=\"UpDownOperator\" weight=\"3.0\">
        <parameter idref=\"ucldMean.c:FILENAME\" name=\"up\"/>
        <tree idref=\"Tree.t:FILENAME\" name=\"down\"/>
    </operator>
    <operator id=\"PopSizeScaler.t:FILENAME\" parameter=\"@popSize.t:FILENAME\" scaleFactor=\"0.75\" spec=\"ScaleOperator\" weight=\"3.0\"/>"

block7 <- "    <logger fileName=\"FILENAME.log\" id=\"tracelog\" logEvery=\"1000\" model=\"@posterior\" sanitiseHeaders=\"true\" sort=\"smart\">
        <log idref=\"posterior\"/>
        <log idref=\"likelihood\"/>
        <log idref=\"prior\"/>
        <log idref=\"treeLikelihood.FILENAME\"/>
        <log id=\"TreeHeight.t:FILENAME\" spec=\"beast.evolution.tree.TreeHeightLogger\" tree=\"@Tree.t:FILENAME\"/>
        <parameter idref=\"ucldMean.c:FILENAME\" name=\"log\"/>
        <parameter idref=\"ucldStdev.c:FILENAME\" name=\"log\"/>
        <log branchratemodel=\"@RelaxedClock.c:FILENAME\" id=\"rate.c:FILENAME\" spec=\"beast.evolution.branchratemodel.RateStatistic\" tree=\"@Tree.t:FILENAME\"/>
        <parameter idref=\"popSize.t:FILENAME\" name=\"log\"/>
        <log idref=\"CoalescentConstant.t:FILENAME\"/>
    </logger>
    <logger id=\"screenlog\" logEvery=\"1000\">
        <log idref=\"posterior\"/>
        <log arg=\"@posterior\" id=\"ESS.0\" spec=\"util.ESS\"/>
        <log idref=\"likelihood\"/>
        <log idref=\"prior\"/>
    </logger>
<!--
    <logger fileName=\"$(tree).trees\" id=\"treelog.t:FILENAME\" logEvery=\"1000\" mode=\"tree\">
        <log branchratemodel=\"@RelaxedClock.c:FILENAME\" id=\"TreeWithMetaDataLogger.t:FILENAME\" spec=\"beast.evolution.tree.TreeWithMetaDataLogger\" tree=\"@Tree.t:FILENAME\"/>
    </logger>
-->
</run>
</beast>"

res_out <- paste(block1, taxon_block, block2, block3, date_block,  block4, block5, block6, block7, collapse = '\n')
res_out <- gsub('FILENAME', file_name, res_out)
return(res_out)

}




####################
# Run BEAST and collect data
####################


run_beast <- function(file_name = '', beast_path = '', temp_name = 'out_temp.tree'){
	  system(paste0(beast_path, ' ', file_name))
#####
	#  system(paste0(beast_path, 'treeannotator ', gsub('xml', 'trees ', file_name), temp_name))
#####
	  dat_temp <- read.table(gsub('xml', 'log', file_name), head = T, as.is = T)
	  rate_est <- mean(as.numeric(dat_temp$ucldMean))
	  rate_hpd <- quantile(as.numeric(dat_temp$ucldMean), c(0.025, 0.975))
	  root_est <- mean(as.numeric(dat_temp$TreeHeight))
	  root_hpd <- quantile(as.numeric(dat_temp$TreeHeight), c(0.025, 0.975))
	  
########
	  #tree_est <- read.annotated.nexus(temp_name)
	  #dat_mat_est <- trann2trdat(tree_est)
	  #est_phylogram <- tree_est
	  #est_phylogram$edge.length <- dat_mat_est[, 6]
	  #dates <- as.numeric(gsub('^.+_', '', est_phylogram$tip.label))
	  #root_tips <- allnode.times(est_phylogram, tipsonly = T)	  

	  #lin_temp <- summary(lm(root_tips ~ dates + 0))
	  #r_est <- lin_temp$r.squared
	  #slope_est <- lin_temp$coefficients[1]
######
	  #return(list(rate_est = rate_est, rate_hpd = rate_hpd, root_est = root_est, root_hpd = root_hpd, slope_est = slope_est, r_est = r_est))
	  return(list(rate_est = rate_est, rate_hpd = rate_hpd, root_est = root_est, root_hpd = root_hpd))
	  
}






