#!/usr/bin/python

ucld_clock = '''<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><beast beautitemplate='Standard' beautistatus='' namespace=\"beast.core:beast.evolution.alignment:beast.evolution.tree.coalescent:beast.core.util:beast.evolution.nuc:beast.evolution.operators:beast.evolution.sitemodel:beast.evolution.substitutionmodel:beast.evolution.likelihood\" version=\"2.0\">
    <data
id=\"sequence_data\"
name=\"alignment\">
<!--INPUT_SEQUENCE_DATA-->
                </data>
    
<map name=\"Uniform\" >beast.math.distributions.Uniform</map>
<map name=\"Exponential\" >beast.math.distributions.Exponential</map>
<map name=\"LogNormal\" >beast.math.distributions.LogNormalDistributionModel</map>
<map name=\"Normal\" >beast.math.distributions.Normal</map>
<map name=\"Beta\" >beast.math.distributions.Beta</map>
<map name=\"Gamma\" >beast.math.distributions.Gamma</map>
<map name=\"LaplaceDistribution\" >beast.math.distributions.LaplaceDistribution</map>
<map name=\"prior\" >beast.math.distributions.Prior</map>
<map name=\"InverseGamma\" >beast.math.distributions.InverseGamma</map>
<map name=\"OneOnX\" >beast.math.distributions.OneOnX</map>

<run id=\"mcmc\" spec=\"MCMC\" chainLength=\"20000000\">
    <state id=\"state\" storeEvery=\"5000\">
        <tree id=\"Tree.t:sequence_data\" name=\"stateNode\">
            <taxonset id=\"TaxonSet.sequence_data\" spec=\"TaxonSet\">
                <alignment idref=\"sequence_data\"/>
            </taxonset>
        </tree>
        <parameter id=\"birthRate2.t:sequence_data\" lower=\"0.0\" name=\"stateNode\" upper=\"10000.0\">1.0</parameter>
        <parameter id=\"relativeDeathRate2.t:sequence_data\" lower=\"0.0\" name=\"stateNode\" upper=\"1.0\">0.5</parameter>
        <parameter id=\"ucldMean.c:sequence_data\" name=\"stateNode\">1.0</parameter>
        <parameter id=\"ucldStdev.c:sequence_data\" lower=\"0.0\" name=\"stateNode\">0.1</parameter>
        <stateNode id=\"rateCategories.c:sequence_data\" spec=\"parameter.IntegerParameter\" dimension=\"18\">1</stateNode>
    </state>

    <init id=\"RandomTree.t:sequence_data\" spec=\"beast.evolution.tree.RandomTree\" estimate=\"false\" initial=\"@Tree.t:sequence_data\" taxa=\"@sequence_data\">
        <populationModel id=\"ConstantPopulation0.t:sequence_data\" spec=\"ConstantPopulation\">
            <parameter id=\"randomPopSize.t:sequence_data\" name=\"popSize\">1.0</parameter>
        </populationModel>
    </init>

    <distribution id=\"posterior\" spec=\"util.CompoundDistribution\">
        <distribution id=\"prior\" spec=\"util.CompoundDistribution\">
            <distribution id=\"BirthDeath.t:sequence_data\" spec=\"beast.evolution.speciation.BirthDeathGernhard08Model\" birthDiffRate=\"@birthRate2.t:sequence_data\" relativeDeathRate=\"@relativeDeathRate2.t:sequence_data\" tree=\"@Tree.t:sequence_data\"/>
            <prior id=\"BirthRatePrior.t:sequence_data\" name=\"distribution\" x=\"@birthRate2.t:sequence_data\">
                <Uniform id=\"Uniform.0\" name=\"distr\" upper=\"1000.0\"/>
            </prior>
            <prior id=\"DeathRatePrior.t:sequence_data\" name=\"distribution\" x=\"@relativeDeathRate2.t:sequence_data\">
                <Uniform id=\"Uniform.01\" name=\"distr\"/>
            </prior>
            <distribution id=\"all.prior\" spec=\"beast.math.distributions.MRCAPrior\" monophyletic=\"true\" tree=\"@Tree.t:sequence_data\">
                <taxonset id=\"all\" spec=\"TaxonSet\">
                    <taxon id=\"t1\" spec=\"Taxon\"/>
                    <taxon id=\"t10\" spec=\"Taxon\"/>
                    <taxon id=\"t2\" spec=\"Taxon\"/>
                    <taxon id=\"t3\" spec=\"Taxon\"/>
                    <taxon id=\"t4\" spec=\"Taxon\"/>
                    <taxon id=\"t5\" spec=\"Taxon\"/>
                    <taxon id=\"t6\" spec=\"Taxon\"/>
                    <taxon id=\"t7\" spec=\"Taxon\"/>
                    <taxon id=\"t8\" spec=\"Taxon\"/>
                    <taxon id=\"t9\" spec=\"Taxon\"/>
                </taxonset>
                <Normal id=\"Normal.0\" name=\"distr\">
                    <parameter id=\"RealParameter.0\" estimate=\"false\" name=\"mean\">100.0</parameter>
                    <parameter id=\"RealParameter.01\" estimate=\"false\" name=\"sigma\">0.5</parameter>
                </Normal>
            </distribution>
            <prior id=\"ucldStdevPrior.c:sequence_data\" name=\"distribution\" x=\"@ucldStdev.c:sequence_data\">
                <Gamma id=\"Gamma.0\" name=\"distr\">
                    <parameter id=\"RealParameter.02\" estimate=\"false\" name=\"alpha\">0.5396</parameter>
                    <parameter id=\"RealParameter.03\" estimate=\"false\" name=\"beta\">0.3819</parameter>
                </Gamma>
            </prior>
            <prior id=\"MeanRatePrior.c:sequence_data\" name=\"distribution\" x=\"@ucldMean.c:sequence_data\">
                <Uniform id=\"Uniform.02\" name=\"distr\" upper=\"Infinity\"/>
            </prior>
        </distribution>
        <distribution id=\"likelihood\" spec=\"util.CompoundDistribution\">
            <distribution id=\"treeLikelihood.sequence_data\" spec=\"TreeLikelihood\" data=\"@sequence_data\" tree=\"@Tree.t:sequence_data\">
                <siteModel id=\"SiteModel.s:sequence_data\" spec=\"SiteModel\">
                    <parameter id=\"mutationRate.s:sequence_data\" estimate=\"false\" name=\"mutationRate\">1.0</parameter>
                    <parameter id=\"gammaShape.s:sequence_data\" estimate=\"false\" name=\"shape\">1.0</parameter>
                    <parameter id=\"proportionInvariant.s:sequence_data\" estimate=\"false\" lower=\"0.0\" name=\"proportionInvariant\" upper=\"1.0\">0.0</parameter>
                    <substModel id=\"JC69.s:sequence_data\" spec=\"JukesCantor\"/>
                </siteModel>
                <branchRateModel id=\"RelaxedClock.c:sequence_data\" spec=\"beast.evolution.branchratemodel.UCRelaxedClockModel\" clock.rate=\"@ucldMean.c:sequence_data\" rateCategories=\"@rateCategories.c:sequence_data\" tree=\"@Tree.t:sequence_data\">
                    <LogNormal id=\"LogNormalDistributionModel.c:sequence_data\" S=\"@ucldStdev.c:sequence_data\" meanInRealSpace=\"true\" name=\"distr\">
                        <parameter id=\"RealParameter.04\" estimate=\"false\" lower=\"0.0\" name=\"M\" upper=\"1.0\">1.0</parameter>
                    </LogNormal>
                </branchRateModel>
            </distribution>
        </distribution>
    </distribution>

    <operator id=\"BirthDeathTreeScaler.t:sequence_data\" spec=\"ScaleOperator\" scaleFactor=\"0.5\" tree=\"@Tree.t:sequence_data\" weight=\"3.0\"/>

    <operator id=\"BirthDeathTreeRootScaler.t:sequence_data\" spec=\"ScaleOperator\" rootOnly=\"true\" scaleFactor=\"0.5\" tree=\"@Tree.t:sequence_data\" weight=\"3.0\"/>

    <operator id=\"BirthDeathUniformOperator.t:sequence_data\" spec=\"Uniform\" tree=\"@Tree.t:sequence_data\" weight=\"30.0\"/>

    <operator id=\"BirthDeathSubtreeSlide.t:sequence_data\" spec=\"SubtreeSlide\" tree=\"@Tree.t:sequence_data\" weight=\"15.0\"/>

    <operator id=\"BirthDeathNarrow.t:sequence_data\" spec=\"Exchange\" tree=\"@Tree.t:sequence_data\" weight=\"15.0\"/>

    <operator id=\"BirthDeathWide.t:sequence_data\" spec=\"Exchange\" isNarrow=\"false\" tree=\"@Tree.t:sequence_data\" weight=\"3.0\"/>

    <operator id=\"BirthDeathWilsonBalding.t:sequence_data\" spec=\"WilsonBalding\" tree=\"@Tree.t:sequence_data\" weight=\"3.0\"/>

    <operator id=\"BirthRateScaler.t:sequence_data\" spec=\"ScaleOperator\" parameter=\"@birthRate2.t:sequence_data\" scaleFactor=\"0.75\" weight=\"3.0\"/>

    <operator id=\"DeathRateScaler.t:sequence_data\" spec=\"ScaleOperator\" parameter=\"@relativeDeathRate2.t:sequence_data\" scaleFactor=\"0.75\" weight=\"3.0\"/>

    <operator id=\"ucldMeanScaler.c:sequence_data\" spec=\"ScaleOperator\" parameter=\"@ucldMean.c:sequence_data\" scaleFactor=\"0.5\" weight=\"1.0\"/>

    <operator id=\"ucldStdevScaler.c:sequence_data\" spec=\"ScaleOperator\" parameter=\"@ucldStdev.c:sequence_data\" scaleFactor=\"0.5\" weight=\"3.0\"/>

    <operator id=\"CategoriesRandomWalk.c:sequence_data\" spec=\"IntRandomWalkOperator\" parameter=\"@rateCategories.c:sequence_data\" weight=\"10.0\" windowSize=\"1\"/>

    <operator id=\"CategoriesSwapOperator.c:sequence_data\" spec=\"SwapOperator\" intparameter=\"@rateCategories.c:sequence_data\" weight=\"10.0\"/>

    <operator id=\"CategoriesUniform.c:sequence_data\" spec=\"UniformOperator\" parameter=\"@rateCategories.c:sequence_data\" weight=\"10.0\"/>

    <operator id=\"relaxedUpDownOperator.c:sequence_data\" spec=\"UpDownOperator\" scaleFactor=\"0.75\" weight=\"3.0\">
        <up idref=\"ucldMean.c:sequence_data\"/>
        <down idref=\"Tree.t:sequence_data\"/>
    </operator>

    <logger id=\"tracelog\" fileName=\"OUT_FILE_NAME.log\" logEvery=\"1000\" model=\"@posterior\" sanitiseHeaders=\"true\" sort=\"smart\">
        <log idref=\"posterior\"/>
        <log idref=\"likelihood\"/>
        <log idref=\"prior\"/>
        <log idref=\"treeLikelihood.sequence_data\"/>
        <log id=\"TreeHeight.t:sequence_data\" spec=\"beast.evolution.tree.TreeHeightLogger\" tree=\"@Tree.t:sequence_data\"/>
        <log idref=\"BirthDeath.t:sequence_data\"/>
        <log idref=\"birthRate2.t:sequence_data\"/>
        <log idref=\"relativeDeathRate2.t:sequence_data\"/>
        <log idref=\"all.prior\"/>
        <log idref=\"ucldMean.c:sequence_data\"/>
        <log idref=\"ucldStdev.c:sequence_data\"/>
        <log id=\"rate.c:sequence_data\" spec=\"beast.evolution.branchratemodel.RateStatistic\" branchratemodel=\"@RelaxedClock.c:sequence_data\" tree=\"@Tree.t:sequence_data\"/>
    </logger>

    <logger id=\"screenlog\" logEvery=\"1000\">
        <log idref=\"posterior\"/>
        <log id=\"ESS.0\" spec=\"util.ESS\" arg=\"@posterior\"/>
        <log idref=\"likelihood\"/>
        <log idref=\"prior\"/>
    </logger>

    <logger id=\"treelog.t:sequence_data\" fileName=\"OUT_FILE_NAME.trees\" logEvery=\"1000\" mode=\"tree\">
        <log id=\"TreeWithMetaDataLogger.t:sequence_data\" spec=\"beast.evolution.tree.TreeWithMetaDataLogger\" branchratemodel=\"@RelaxedClock.c:sequence_data\" tree=\"@Tree.t:sequence_data\"/>
    </logger>

</run>

</beast>
'''

strict_clock = '''<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><beast beautitemplate='Standard' beautistatus='' namespace=\"beast.core:beast.evolution.alignment:beast.evolution.tree.coalescent:beast.core.util:beast.evolution.nuc:beast.evolution.operators:beast.evolution.sitemodel:beast.evolution.substitutionmodel:beast.evolution.likelihood\" version=\"2.0\">

    <data
id=\"sequence_data\"
name=\"alignment\">
<!--INPUT_SEQUENCE_DATA-->
</data>
<map name=\"Uniform\" >beast.math.distributions.Uniform</map>
<map name=\"Exponential\" >beast.math.distributions.Exponential</map>
<map name=\"LogNormal\" >beast.math.distributions.LogNormalDistributionModel</map>
<map name=\"Normal\" >beast.math.distributions.Normal</map>
<map name=\"Beta\" >beast.math.distributions.Beta</map>
<map name=\"Gamma\" >beast.math.distributions.Gamma</map>
<map name=\"LaplaceDistribution\" >beast.math.distributions.LaplaceDistribution</map>
<map name=\"prior\" >beast.math.distributions.Prior</map>
<map name=\"InverseGamma\" >beast.math.distributions.InverseGamma</map>
<map name=\"OneOnX\" >beast.math.distributions.OneOnX</map>

<run id=\"mcmc\" spec=\"MCMC\" chainLength=\"20000000\">
    <state id=\"state\" storeEvery=\"5000\">
        <tree id=\"Tree.t:sequence_data\" name=\"stateNode\">
            <taxonset id=\"TaxonSet.sequence_data\" spec=\"TaxonSet\">
                <alignment idref=\"sequence_data\"/>
            </taxonset>
        </tree>
        <parameter id=\"birthRate2.t:sequence_data\" lower=\"0.0\" name=\"stateNode\" upper=\"10000.0\">1.0</parameter>
        <parameter id=\"relativeDeathRate2.t:sequence_data\" lower=\"0.0\" name=\"stateNode\" upper=\"1.0\">0.5</parameter>
        <parameter id=\"clockRate.c:sequence_data\" name=\"stateNode\">1.0</parameter>
    </state>

    <init id=\"RandomTree.t:sequence_data\" spec=\"beast.evolution.tree.RandomTree\" estimate=\"false\" initial=\"@Tree.t:sequence_data\" taxa=\"@sequence_data\">
        <populationModel id=\"ConstantPopulation0.t:sequence_data\" spec=\"ConstantPopulation\">
            <parameter id=\"randomPopSize.t:sequence_data\" name=\"popSize\">1.0</parameter>
        </populationModel>
    </init>

    <distribution id=\"posterior\" spec=\"util.CompoundDistribution\">
        <distribution id=\"prior\" spec=\"util.CompoundDistribution\">
            <distribution id=\"BirthDeath.t:sequence_data\" spec=\"beast.evolution.speciation.BirthDeathGernhard08Model\" birthDiffRate=\"@birthRate2.t:sequence_data\" relativeDeathRate=\"@relativeDeathRate2.t:sequence_data\" tree=\"@Tree.t:sequence_data\"/>
            <prior id=\"BirthRatePrior.t:sequence_data\" name=\"distribution\" x=\"@birthRate2.t:sequence_data\">
                <Uniform id=\"Uniform.0\" name=\"distr\" upper=\"1000.0\"/>
            </prior>
            <prior id=\"ClockPrior.c:sequence_data\" name=\"distribution\" x=\"@clockRate.c:sequence_data\">
                <Uniform id=\"Uniform.01\" name=\"distr\" upper=\"Infinity\"/>
            </prior>
            <prior id=\"DeathRatePrior.t:sequence_data\" name=\"distribution\" x=\"@relativeDeathRate2.t:sequence_data\">
                <Uniform id=\"Uniform.02\" name=\"distr\"/>
            </prior>
            <distribution id=\"all.prior\" spec=\"beast.math.distributions.MRCAPrior\" monophyletic=\"true\" tree=\"@Tree.t:sequence_data\">
                <taxonset id=\"all\" spec=\"TaxonSet\">
<!-- THIS NEEDS TO BE CHANGED FOR DATA SETS WITH MORE THAN 10 TAXA -->
                    <taxon id=\"t1\" spec=\"Taxon\"/>
                    <taxon id=\"t10\" spec=\"Taxon\"/>
                    <taxon id=\"t2\" spec=\"Taxon\"/>
                    <taxon id=\"t3\" spec=\"Taxon\"/>
                    <taxon id=\"t4\" spec=\"Taxon\"/>
                    <taxon id=\"t5\" spec=\"Taxon\"/>
                    <taxon id=\"t6\" spec=\"Taxon\"/>
                    <taxon id=\"t7\" spec=\"Taxon\"/>
                    <taxon id=\"t8\" spec=\"Taxon\"/>
                    <taxon id=\"t9\" spec=\"Taxon\"/>

                </taxonset>
                <Normal id=\"Normal.0\" name=\"distr\">
                    <parameter id=\"RealParameter.0\" estimate=\"false\" name=\"mean\">100.0</parameter>
                    <parameter id=\"RealParameter.01\" estimate=\"false\" name=\"sigma\">0.5</parameter>
                </Normal>
            </distribution>
        </distribution>
        <distribution id=\"likelihood\" spec=\"util.CompoundDistribution\">
            <distribution id=\"treeLikelihood.sequence_data\" spec=\"TreeLikelihood\" data=\"@sequence_data\" tree=\"@Tree.t:sequence_data\">
                <siteModel id=\"SiteModel.s:sequence_data\" spec=\"SiteModel\">
                    <parameter id=\"mutationRate.s:sequence_data\" estimate=\"false\" name=\"mutationRate\">1.0</parameter>
                    <parameter id=\"gammaShape.s:sequence_data\" estimate=\"false\" name=\"shape\">1.0</parameter>
                    <parameter id=\"proportionInvariant.s:sequence_data\" estimate=\"false\" lower=\"0.0\" name=\"proportionInvariant\" upper=\"1.0\">0.0</parameter>
                    <substModel id=\"JC69.s:sequence_data\" spec=\"JukesCantor\"/>
                </siteModel>
                <branchRateModel id=\"StrictClock.c:sequence_data\" spec=\"beast.evolution.branchratemodel.StrictClockModel\" clock.rate=\"@clockRate.c:sequence_data\"/>
            </distribution>
        </distribution>
    </distribution>

    <operator id=\"BirthDeathTreeScaler.t:sequence_data\" spec=\"ScaleOperator\" scaleFactor=\"0.5\" tree=\"@Tree.t:sequence_data\" weight=\"3.0\"/>

    <operator id=\"BirthDeathTreeRootScaler.t:sequence_data\" spec=\"ScaleOperator\" rootOnly=\"true\" scaleFactor=\"0.5\" tree=\"@Tree.t:sequence_data\" weight=\"3.0\"/>

    <operator id=\"BirthDeathUniformOperator.t:sequence_data\" spec=\"Uniform\" tree=\"@Tree.t:sequence_data\" weight=\"30.0\"/>

    <operator id=\"BirthDeathSubtreeSlide.t:sequence_data\" spec=\"SubtreeSlide\" tree=\"@Tree.t:sequence_data\" weight=\"15.0\"/>

    <operator id=\"BirthDeathNarrow.t:sequence_data\" spec=\"Exchange\" tree=\"@Tree.t:sequence_data\" weight=\"15.0\"/>

    <operator id=\"BirthDeathWide.t:sequence_data\" spec=\"Exchange\" isNarrow=\"false\" tree=\"@Tree.t:sequence_data\" weight=\"3.0\"/>

    <operator id=\"BirthDeathWilsonBalding.t:sequence_data\" spec=\"WilsonBalding\" tree=\"@Tree.t:sequence_data\" weight=\"3.0\"/>

    <operator id=\"BirthRateScaler.t:sequence_data\" spec=\"ScaleOperator\" parameter=\"@birthRate2.t:sequence_data\" scaleFactor=\"0.75\" weight=\"3.0\"/>

    <operator id=\"DeathRateScaler.t:sequence_data\" spec=\"ScaleOperator\" parameter=\"@relativeDeathRate2.t:sequence_data\" scaleFactor=\"0.75\" weight=\"3.0\"/>

    <operator id=\"StrictClockRateScaler.c:sequence_data\" spec=\"ScaleOperator\" parameter=\"@clockRate.c:sequence_data\" scaleFactor=\"0.75\" weight=\"3.0\"/>

    <operator id=\"strictClockUpDownOperator.c:sequence_data\" spec=\"UpDownOperator\" scaleFactor=\"0.75\" weight=\"3.0\">
        <up idref=\"clockRate.c:sequence_data\"/>
        <down idref=\"Tree.t:sequence_data\"/>
    </operator>
    <logger id=\"tracelog\" fileName=\"OUT_FILE_NAME.log\" logEvery=\"1000\" model=\"@posterior\" sanitiseHeaders=\"true\" sort=\"smart\">
        <log idref=\"posterior\"/>
        <log idref=\"likelihood\"/>
        <log idref=\"prior\"/>
        <log idref=\"treeLikelihood.sequence_data\"/>
        <log id=\"TreeHeight.t:sequence_data\" spec=\"beast.evolution.tree.TreeHeightLogger\" tree=\"@Tree.t:sequence_data\"/>
        <log idref=\"BirthDeath.t:sequence_data\"/>
        <log idref=\"birthRate2.t:sequence_data\"/>
        <log idref=\"relativeDeathRate2.t:sequence_data\"/>
        <log idref=\"all.prior\"/>
        <log idref=\"clockRate.c:sequence_data\"/>
    </logger>
    <logger id=\"screenlog\" logEvery=\"1000\">
        <log idref=\"posterior\"/>
        <log id=\"ESS.0\" spec=\"util.ESS\" arg=\"@posterior\"/>
        <log idref=\"likelihood\"/>
        <log idref=\"prior\"/>
    </logger>
    <logger id=\"treelog.t:sequence_data\" fileName=\"OUT_FILE_NAME.trees\" logEvery=\"1000\" mode=\"tree\">
        <log id=\"TreeWithMetaDataLogger.t:sequence_data\" spec=\"beast.evolution.tree.TreeWithMetaDataLogger\" tree=\"@Tree.t:sequence_data\"/>
    </logger>
</run>
</beast>
'''

import re, sys

def fasta_to_dict(fasta_file):
    fasta_lines = open(fasta_file).readlines()
    t_names = [re.sub('>|\n', '', i) for i in fasta_lines if '>' in i]
    secs = [re.sub('\n', '', i) for i in fasta_lines if not '>' in i]

    dict_secs = {}
    for t, s in zip(t_names, secs):
        dict_secs[t] = s
    return dict_secs


#NOW INPUT FILE NAMES 
#input_file = 's2_strict_subset.fasta'
input_file = sys.argv[1]
print sys.argv[1]

def make_strict(input_file):
    secs_data = fasta_to_dict(input_file)
    taxon_blocks = list()

    for TAXON in secs_data:
        SEQUENCE = secs_data[TAXON]
        taxon_blocks.append("<sequence id=\"seq_"+TAXON+"\" taxon=\""+TAXON+"\" totalcount=\"4\" value=\""+SEQUENCE+"\"/>")

    taxon_block = '\n'.join(taxon_blocks)
    strict_step_1 = re.sub('<!--INPUT_SEQUENCE_DATA-->', taxon_block, strict_clock)
    out_file_name = re.sub('[.].+', '_strict', input_file)
    strict_step_2 = re.sub('OUT_FILE_NAME', out_file_name, strict_step_1)
    
    open(out_file_name+'.xml', 'w').writelines(strict_step_2)

def make_ucld(input_file):
    secs_data = fasta_to_dict(input_file)
    taxon_blocks = list()

    for TAXON in secs_data:
        SEQUENCE = secs_data[TAXON]
        taxon_blocks.append("<sequence id=\"seq_"+TAXON+"\" taxon=\""+TAXON+"\" totalcount=\"4\" value=\""+SEQUENCE+"\"/>")

    taxon_block = '\n'.join(taxon_blocks)
    ucld_step_1 = re.sub('<!--INPUT_SEQUENCE_DATA-->', taxon_block, ucld_clock)
    out_file_name = re.sub('[.].+', '_ucld', input_file)
    ucld_step_2 = re.sub('OUT_FILE_NAME', out_file_name, ucld_step_1)

    open(out_file_name+'.xml', 'w').writelines(ucld_step_2)


make_strict(input_file)
make_ucld(input_file)

