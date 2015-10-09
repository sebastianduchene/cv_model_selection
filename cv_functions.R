
phylo_likelihood <- function(nex_data_file, log_file, trees_file, train_indices = 0, post_samples= NULL, test_type = 'ml'){
    #Only works for GTR+G
    require(phangorn)
    data <- as.DNAbin(read.nexus.data(nex_data_file))
    if(length(train_indices) != 0){
        data <- as.matrix(data)[, -train_indices]
    }
    data <- phyDat(data)
    trees <- read.nexus(trees_file)
    log_file <- read.table(log_file, head = T, skip = 1)
    if(dim(log_file)[1] != length(trees)) stop('the number of posterior samples and trees differ')
    Qs <- cbind(log_file$r.A...C, log_file$r.A...G, log_file$r.A...T, log_file$r.C...G,  log_file$r.C...T, log_file$r.G...T)
    bfs <- cbind(log_file$pi.A, log_file$pi.C, log_file$pi.G, log_file$pi.T)
    log_liks <- vector()
    if(is.null(post_samples)){
        samples <- tail(1:nrow(log_file), 200)
    }else{
        samples <- post_samples
    }

    if(test_type != 'ml'){
        for(i in samples){
            tr_temp <- trees[[i]]
            log_temp <-  pml(tr_temp, data, Q = Qs[i, ], bf = bfs[i, ])
            log_liks <- c(log_liks, log_temp$logLik)
        }
    }else{
        #find highest lik row. This is giving the model its best chance at predicting future observations
        i_ml <- which.max(log_file$LnL)
        tree_ml <- trees[[i_ml]]
        lik_test <- pml(tree_ml, data, Q = colMeans(Qs), bf = colMeans(bfs))
    }

    if(test_type == 'deltaL'){
        return(abs(median(log_liks) - median(log_file$LnL[samples])))
    }else if(test_type == 'testL'){
        return(log_liks)
    }else if(test_type == 'ml'){
        return(lik_test$logLik)
    }
}

#phylo_likelihood('ss/new_SC_UCL_3.nex', 'ss/new_SC_UCL_train3.nex.p', 'ss/new_SC_UCL_train3.nex.t', test_indices = c(1, 2, 3))

make_mrbayes_block <- function(seq_data, file_name, clock_model = 'strict', ss = T){
    require(ape)
# If training  == T. select only the indexed data to create the nexus file. Note that these are the training indices, not those for hte test set
    names_dates <- matrix(NA, nrow(seq_data), 2)
    names_dates[, 1] <- rownames(seq_data)
    names_split <- strsplit(rownames(seq_data), '_')

    for(i in 1:length(names_split)){
        names_dates[i, 2] <- names_split[[i]][2]
    }

    calibrations <- vector()
    calibrations[1] <- 'begin Mrbayes;\ncalibrate\n'
    for(i in 1:nrow(names_dates)){
        calibrations[i+1] <- paste0(names_dates[i, 1], '=', 'fixed(', names_dates[i, 2], ')')
    }
    calibrations <- c(calibrations, ';\n')

    if(any(clock_model %in% c('strict', 'igr', 'tk02'))){
    model_template <- gsub('CLOCK_MODEL', clock_model, 'prset brlenspr=clock:uniform;\nprset clockvarpr=CLOCK_MODEL;\nprset nodeagepr=calibrated;\nprset clockratepr = normal(0.01,0.005);\nlset rates=gamma nst=6;\nlset nst = 6;\n')
    }else{
        stop('please select a clock model: strict, igr, tk02')
    }

    #SELECT one of the options below
    ss_config <-'ss nsteps=100 ngen=1000000;\nsumss;\nend;\n'
    train_config <- 'mcmcp ngen=10000000 diagnfreq=10000 samplefreq=10000 printfreq= 10000 Nruns=1;\n mcmc;\nend;\n'
    write.nexus.data(seq_data, file_name)

    if(ss){
        cat(c(calibrations, model_template, ss_config), file = file_name, append = T)
    }else{
        cat(c(calibrations, model_template, train_config), file = file_name, append = T)
     }
}


