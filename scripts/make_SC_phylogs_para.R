library(ape)
library(NELSI)
library(foreach)
library(doParallel)



proc_trees <- function(r){
    log_temp <- read.table(strict_clocks[r], head = T)
    log_temp <- log_temp[(nrow(log_temp) - 100):nrow(log_temp), ]
    tree_temp <- read.nexus(gsub('log', 'trees', strict_clocks[r]))
    tree_temp <- tree_temp[(length(tree_temp) - 100):length(tree_temp)] 
    
    phylogs_temp <- list()
    for(t in 1:length(tree_temp)){
        phylogs_temp[[t]] <- tree_temp[[t]]
        phylogs_temp[[t]]$edge.length <- tree_temp[[t]]$edge.length * log_temp$clockRate[t]
    }
    class(phylogs_temp) <- 'multiPhylo'
    write.tree(phylogs_temp, file = gsub('[.]log', '_phylogs.trees', strict_clocks[r]))
}

strict_clocks <- paste0('runs/', dir('runs/', pattern = 'strict[.]log'))

# modify to run only last 100 trees
#for(i in 1:length(strict_clocks)){
#      print(strict_clocks[i])
#      proc_trees(i)
#}
cl <- makeCluster(7)
registerDoParallel(cl)

get_phylogs <- foreach(x = 1:length(strict_clocks), .packages = 'ape') %dopar% proc_trees(x)

stopCluster(cl)