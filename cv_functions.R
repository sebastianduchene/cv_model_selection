
phylo_likelihood <- function(nex_data_file, log_file, trees_file, test_indices = 0){
    #Only works for GTR+G
    require(phangorn)
    data <- as.DNAbin(read.nexus.data(nex_data_file))
    if(length(test_indices) != 0){
        data <- as.matrix(data)[, test_indices]
    }
    data <- phyDat(data)
    trees <- read.nexus(trees_file)
    log_file <- read.table(log_file, head = T, skip = 1)
    if(dim(log_file)[1] != length(trees)) stop('the number of posterior samples and trees differ')
    Qs <- cbind(log_file$r.A...C, log_file$r.A...G, log_file$r.A...T, log_file$r.C...G,  log_file$r.C...T, log_file$r.G...T)
    bfs <- cbind(log_file$pi.A, log_file$pi.C, log_file$pi.G, log_file$pi.T)
    log_liks <- vector()
    for(i in 1:length(trees)){
        tr_temp <- trees[[i]]
        log_temp <-  pml(tr_temp, data, Q = Qs[i, ], bf = bfs[i, ])
        log_liks[i] <- log_temp$logLik
    }
    return(log_liks)
}

#phylo_likelihood('ss/new_SC_UCL_3.nex', 'ss/new_SC_UCL_train3.nex.p', 'ss/new_SC_UCL_train3.nex.t', test_indices = c(1, 2, 3))

make_mrbayes_block <- function(seq_data, file_name, clock_model = 'strict', ss = T){
    require(ape)
# If training  == T. select only the indexed data to create the nexus file. Note that these are the training indices, not those for hte test set
    calibrations <- 'begin Mrbayes;\ncalibrate\nt1_7.58=fixed(7.58)\nt2_1.33=fixed(1.33)\nt3_7=fixed(7)\nt4_5=fixed(5)\nt5_11=fixed(11)\nt6_3=fixed(3)\nt7_8.75=fixed(8.75)\nt8_13.17=fixed(13.17)\nt9_1=fixed(1)\nt10_5.75=fixed(5.75)\nt11_11.08=fixed(11.08)\nt12_0.42=fixed(0.42)\nt13_6.25=fixed(6.25)\nt14_5.33=fixed(5.33)\nt15_8.92=fixed(8.92)\nt16_6=fixed(6)\nt17_11.25=fixed(11.25)\nt18_3.5=fixed(3.5)\nt19_3=fixed(3)\nt20_8.5=fixed(8.5)\nt21_9.92=fixed(9.92)\nt22_2.33=fixed(2.33)\nt23_11.67=fixed(11.67)\nt24_7.67=fixed(7.67)\nt25_6.08=fixed(6.08)\nt26_6.92=fixed(6.92)\nt27_4.25=fixed(4.25)\nt28_8.92=fixed(8.92)\nt29_3.67=fixed(3.67)\nt30_8.83=fixed(8.83)\nt31_1.5=fixed(1.5)\nt32_0=fixed(0)\nt33_4.92=fixed(4.92)\nt34_0.08=fixed(0.08)\nt35_6.5=fixed(6.5)\nt36_11.42=fixed(11.42)\nt37_7.42=fixed(7.42)\nt38_4.75=fixed(4.75)\nt39_6.58=fixed(6.58)\nt40_5.92=fixed(5.92)\nt41_11.5=fixed(11.5)\nt42_8.58=fixed(8.58)\nt43_5.5=fixed(5.5)\nt44_11.33=fixed(11.33)\nt45_4=fixed(4)\nt46_8.17=fixed(8.17)\nt47_8.17=fixed(8.17)\nt48_2.5=fixed(2.5)\nt49_2.25=fixed(2.25)\nt50_3.25=fixed(3.25);\n'

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


