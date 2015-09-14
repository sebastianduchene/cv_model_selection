library(ape)

empirical_tree <- read.tree('m_tub_argentina_snps_pruned.phy_phyml_tree')
plot(empirical_tree)

taxa_dates <- data.frame(taxon = empirical_tree$tip.label, date = sapply(all_taxa, function(x) as.numeric(gsub('^.+_', '', x))), sel = F)

taxa_dates$sel[c(which.min(taxa_dates$date), which.max(taxa_dates$date))] <- T

set.seed(12345)
#Keep the oldest and youngest sequences
taxa_dates$sel[sample(seq(1, nrow(taxa_dates))[-c(which.min(taxa_dates$date), which.max(taxa_dates$date))], size = 48)] <- T



complete_data <- read.dna('m_tub_argentina_snps_pruned.fasta', format = 'fasta')

#complete_data[
subset_data <- complete_data[rownames(complete_data) %in% taxa_dates$taxon[taxa_dates$sel], ]

write.dna(subset_data, file = 'm_tub_argentina_CV.fasta', format = 'fasta', nbcol = -1, colsep = '')
write.dna(subset_data, file = 'm_tub_argentina_CV.phy' , nbcol = -1, colsep = '')

# As estimated in BEAST: alpha = 6.85, ac = 0.3, ag = 0.9, at = 0.18, cg = 0.28, gt = 0.33, piA=0.19, piC=0.35, piG=0.31, piT=0.153, TMRCA = 




