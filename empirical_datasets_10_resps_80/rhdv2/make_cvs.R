library(ape)

dat <- read.dna('rhdv2.fasta', format = 'fasta')

dat <- dat[, 1:(ncol(dat) - 1)]


for(i in 1:10){
    sites <- sample(1:ncol(dat), size = 0.8 * ncol(dat))
    training <- dat[, sites]
    test <- dat[, -sites]
    write.dna(training, file = paste0('rhdv2_training_', i, '.fasta'), format = 'fasta', nbcol = -1, colsep = '')
    write.dna(test, file = paste0('rhdv2_test_', i, '.fasta'), format = 'fasta', nbcol = -1, colsep = '')
}

fasta_files <- dir(pattern = 'training_.+fasta')

for(f in fasta_files){
    system(paste('../make_xmls.py', f))
}
