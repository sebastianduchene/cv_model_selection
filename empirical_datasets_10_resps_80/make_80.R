library(ape)
setwd('enterovirus_test')


dat <- read.dna('enterovirus.fasta', format = 'fasta')
dat

dat <- dat[, 1:(ncol(dat)-1)]

for(i in 1:10){
    train_samples <- sample(1:ncol(dat), size = ncol(dat)*0.8)
    training <- dat[, train_samples]
    test <- dat[, -train_samples]
    write.dna(training, file = paste0('enterovirus_training_', i, '.fasta'), format = 'fasta', nbcol = -1, colsep = '')
    write.dna(test, file = paste0('enterovirus_test_', i, '.fasta'), format = 'fasta', nbcol = -1, colsep = '')
}

fastas <- dir(pattern = '.+training.+fasta')
fastas

for(f in fastas){
    system(paste('../make_xmls.py', f))
}
