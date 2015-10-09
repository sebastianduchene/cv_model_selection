library(NELSI)


seq_data <- read.dna('sims_r3/ACL_1.fasta', format = 'fasta')

names_dates <- matrix(NA, nrow(seq_data), 2)
names_dates[, 1] <- rownames(seq_data)
names_split <- strsplit(rownames(seq_data), '_')

for(i in 1:length(names_split)){
    names_dates[i, 2] <- names_split[[i]][2]
}

calibration_block <- vector()
calibration_block[1] <- 'begin Mrbayes;\ncalibrate\n'
for(i in 1:nrow(names_dates)){
    calibration_block[i+1] <- paste0(names_dates[i, 1], '=', 'fixed(', names_dates[i, 2], ')')
}
calibration_block <- c(calibration_block, ';')

