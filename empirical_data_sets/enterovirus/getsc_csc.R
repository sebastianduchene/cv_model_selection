library(phangorn)

log_data <- read.table('enterovir_training2_strict_constant.log', head = T)
log_data <- log_data[(nrow(log_data) - 100):(nrow(log_data)), ]
tree_data <- read.tree('enterovir_training2_strict_constant_phylogs.trees')
print('step1')
test_data <- phyDat(read.dna('enterovir_test2.fasta', format = 'fasta'))
print('loaded data')

get_likelihoods <- function(log_data, tree_data, test_data, model){

    gamma <- log_data$gammaShape
    freqs <- log_data[c('freqParameter.1','freqParameter.2', 'freqParameter.3', 'freqParameter.4')]
    ex_rates <- log_data[c('rateAC', 'rateAG', 'rateAT', 'rateCG' ,'rateGT')]

    liks <- vector()
    for(i in 1:100){
#	print(i)
#	print('params are')
#	print(list(as.numeric(freqs[i, ]), as.numeric(c(ex_rates[i, ], 1)), gamma[i]))
	
	if(model == 'JC'){
		liks[i] <- pml(tree = tree_data[[i]], data= test_data, bf = as.numeric(freqs[i, ]), shape = gamma[i], k = 4)$logLik            
	}else if(model == 'GTR'){
    	liks[i] <- pml(tree = tree_data[[i]], data= test_data, bf = as.numeric(freqs[i, ]), Q = as.numeric(c(ex_rates[i, ], 1)), k = 4, shape = gamma[i])$logLik            
	}
    }
    return(liks)
}

print(get_likelihoods(log_data, tree_data, test_data, model = 'JC'))