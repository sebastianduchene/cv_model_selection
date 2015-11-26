import re, sys


strict_bs = '''<?xml version="1.0" standalone="yes"?>
<beast>
  <taxa id="taxa">
TAXON_DEFINITION_BLOCK
</taxa>

<alignment id="alignment" dataType="nucleotide">
SEQUENCE_DEFINITION_BLOCK
</alignment>
	<patterns id="patterns" from="1" strip="false">
		<alignment idref="alignment"/>
	</patterns>

	<constantSize id="initialDemo" units="years">
		<populationSize>
			<parameter id="initialDemo.popSize" value="100.0"/>
		</populationSize>
	</constantSize>

	<coalescentSimulator id="startingTree">
		<taxa idref="taxa"/>
		<constantSize idref="initialDemo"/>
	</coalescentSimulator>

	<treeModel id="treeModel">
		<coalescentTree idref="startingTree"/>
		<rootHeight>
			<parameter id="treeModel.rootHeight"/>
		</rootHeight>
		<nodeHeights internalNodes="true">
			<parameter id="treeModel.internalNodeHeights"/>
		</nodeHeights>
		<nodeHeights internalNodes="true" rootNode="true">
			<parameter id="treeModel.allInternalNodeHeights"/>
		</nodeHeights>
	</treeModel>

	<generalizedSkyLineLikelihood id="skyline" linear="false">
		<populationSizes>
			<parameter id="skyline.popSize" dimension="10" value="150.0" lower="0.0"/>
		</populationSizes>
		<groupSizes>
			<parameter id="skyline.groupSize" dimension="10"/>
		</groupSizes>
		<populationTree>
			<treeModel idref="treeModel"/>
		</populationTree>
	</generalizedSkyLineLikelihood>
	<exponentialMarkovLikelihood id="eml1" jeffreys="true">
		<chainParameter>
			<parameter idref="skyline.popSize"/>
		</chainParameter>
	</exponentialMarkovLikelihood>

	<strictClockBranchRates id="branchRates">
		<rate>
			<parameter id="clock.rate" value="1.0" lower="0.0"/>
		</rate>
	</strictClockBranchRates>

	<gtrModel id="gtr">
		<frequencies>
			<frequencyModel dataType="nucleotide">
				<frequencies>
					<parameter id="frequencies" value="0.25 0.25 0.25 0.25"/>
				</frequencies>
			</frequencyModel>
		</frequencies>
		<rateAC>
			<parameter id="ac" value="1.0" lower="0.0"/>
		</rateAC>
		<rateAG>
			<parameter id="ag" value="1.0" lower="0.0"/>
		</rateAG>
		<rateAT>
			<parameter id="at" value="1.0" lower="0.0"/>
		</rateAT>
		<rateCG>
			<parameter id="cg" value="1.0" lower="0.0"/>
		</rateCG>
		<rateGT>
			<parameter id="gt" value="1.0" lower="0.0"/>
		</rateGT>
	</gtrModel>

	<siteModel id="siteModel">
		<substitutionModel>
			<gtrModel idref="gtr"/>
		</substitutionModel>
		<gammaShape gammaCategories="4">
			<parameter id="alpha" value="0.5" lower="0.0"/>
		</gammaShape>
	</siteModel>

	<treeLikelihood id="treeLikelihood" useAmbiguities="false">
		<patterns idref="patterns"/>
		<treeModel idref="treeModel"/>
		<siteModel idref="siteModel"/>
		<strictClockBranchRates idref="branchRates"/>
	</treeLikelihood>

	<operators id="operators" optimizationSchedule="default">
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="ac"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="ag"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="at"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="cg"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="gt"/>
		</scaleOperator>
		<deltaExchange delta="0.01" weight="0.1">
			<parameter idref="frequencies"/>
		</deltaExchange>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="alpha"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="3">
			<parameter idref="clock.rate"/>
		</scaleOperator>
		<subtreeSlide size="15.0" gaussian="true" weight="15">
			<treeModel idref="treeModel"/>
		</subtreeSlide>
		<narrowExchange weight="15">
			<treeModel idref="treeModel"/>
		</narrowExchange>
		<wideExchange weight="3">
			<treeModel idref="treeModel"/>
		</wideExchange>
		<wilsonBalding weight="3">
			<treeModel idref="treeModel"/>
		</wilsonBalding>
		<scaleOperator scaleFactor="0.75" weight="3">
			<parameter idref="treeModel.rootHeight"/>
		</scaleOperator>
		<uniformOperator weight="30">
			<parameter idref="treeModel.internalNodeHeights"/>
		</uniformOperator>
		<scaleOperator scaleFactor="0.75" weight="15">
			<parameter idref="skyline.popSize"/>
		</scaleOperator>
		<deltaExchange delta="1" integer="true" weight="6" autoOptimize="false">
			<parameter idref="skyline.groupSize"/>
		</deltaExchange>
		<upDownOperator scaleFactor="0.75" weight="3">
			<up>
				<parameter idref="clock.rate"/>
			</up>
			<down>
				<parameter idref="treeModel.allInternalNodeHeights"/>
			</down>
		</upDownOperator>
	</operators>

	<mcmc id="mcmc" chainLength="100000000" autoOptimize="true">
		<posterior id="posterior">
			<prior id="prior">
				<gammaPrior shape="0.05" scale="10.0" offset="0.0">
					<parameter idref="ac"/>
				</gammaPrior>
				<gammaPrior shape="0.05" scale="20.0" offset="0.0">
					<parameter idref="ag"/>
				</gammaPrior>
				<gammaPrior shape="0.05" scale="10.0" offset="0.0">
					<parameter idref="at"/>
				</gammaPrior>
				<gammaPrior shape="0.05" scale="10.0" offset="0.0">
					<parameter idref="cg"/>
				</gammaPrior>
				<gammaPrior shape="0.05" scale="10.0" offset="0.0">
					<parameter idref="gt"/>
				</gammaPrior>
				<uniformPrior lower="0.0" upper="1.0">
					<parameter idref="frequencies"/>
				</uniformPrior>
				<exponentialPrior mean="0.5" offset="0.0">
					<parameter idref="alpha"/>
				</exponentialPrior>
				<uniformPrior lower="0.0" upper="1.0">
					<parameter idref="clock.rate"/>
				</uniformPrior>
				<uniformPrior lower="0.0" upper="1.0E100">
					<parameter idref="skyline.popSize"/>
				</uniformPrior>
				<generalizedSkyLineLikelihood idref="skyline"/>
				<exponentialMarkovLikelihood idref="eml1"/>
			</prior>
			<likelihood id="likelihood">
				<treeLikelihood idref="treeLikelihood"/>
			</likelihood>
		</posterior>
		<operators idref="operators"/>

		<!-- write log to screen                                                     -->
		<log id="screenLog" logEvery="5000">
			<column label="Posterior" dp="4" width="12">
				<posterior idref="posterior"/>
			</column>
			<column label="Prior" dp="4" width="12">
				<prior idref="prior"/>
			</column>
			<column label="Likelihood" dp="4" width="12">
				<likelihood idref="likelihood"/>
			</column>
			<column label="rootHeight" sf="6" width="12">
				<parameter idref="treeModel.rootHeight"/>
			</column>
			<column label="clock.rate" sf="6" width="12">
				<parameter idref="clock.rate"/>
			</column>
		</log>

		<!-- write log to file                                                       -->
		<log id="fileLog" logEvery="5000" fileName="FILENAME_strict_bs.log" overwrite="false">
			<posterior idref="posterior"/>
			<prior idref="prior"/>
			<likelihood idref="likelihood"/>
			<parameter idref="treeModel.rootHeight"/>
			<parameter idref="skyline.popSize"/>
			<parameter idref="skyline.groupSize"/>
			<parameter idref="ac"/>
			<parameter idref="ag"/>
			<parameter idref="at"/>
			<parameter idref="cg"/>
			<parameter idref="gt"/>
			<parameter idref="frequencies"/>
			<parameter idref="alpha"/>
			<parameter idref="clock.rate"/>
			<treeLikelihood idref="treeLikelihood"/>
			<generalizedSkyLineLikelihood idref="skyline"/>
		</log>

		<logTree id="treeFileLog" logEvery="5000" nexusFormat="true" fileName="FILENAME_strict_bs.trees" sortTranslationTable="true">
			<treeModel idref="treeModel"/>
			<trait name="rate" tag="rate">
				<strictClockBranchRates idref="branchRates"/>
			</trait>
			<posterior idref="posterior"/>
		</logTree>
	</mcmc>

	<marginalLikelihoodEstimator chainLength="10000000" pathSteps="100" pathScheme="betaquantile" alpha="0.3">
		<samplers>
			<mcmc idref="mcmc"/>
		</samplers>
		<pathLikelihood id="pathLikelihood">
			<source>
				<posterior idref="posterior"/>
			</source>
			<destination>
				<prior idref="prior"/>
			</destination>
		</pathLikelihood>
		<log id="MLELog" logEvery="1000" fileName="FILENAME_strict_bs.mle.log">
			<pathLikelihood idref="pathLikelihood"/>
		</log>
	</marginalLikelihoodEstimator>

	<pathSamplingAnalysis fileName="FILENAME_strict_bs.mle.log">
		<likelihoodColumn name="pathLikelihood.delta"/>
		<thetaColumn name="pathLikelihood.theta"/>
	</pathSamplingAnalysis>

	<steppingStoneSamplingAnalysis fileName="FILENAME_strict_bs.mle.log">
		<likelihoodColumn name="pathLikelihood.delta"/>
		<thetaColumn name="pathLikelihood.theta"/>
	</steppingStoneSamplingAnalysis>

	<report>
		<property name="timer">
			<mcmc idref="mcmc"/>
		</property>
	</report>
</beast>
'''

strict_constant = '''<?xml version="1.0" standalone="yes"?>
<beast>
	<taxa id="taxa">
TAXON_DEFINITION_BLOCK
</taxa>

<alignment id="alignment" dataType="nucleotide">
SEQUENCE_DEFINITION_BLOCK
</alignment>

<patterns id="patterns" from="1" strip="false">
<alignment idref="alignment"/>
</patterns>

<constantSize id="constant" units="years">
<populationSize>
<parameter id="constant.popSize" value="150.0" lower="0.0"/>
</populationSize>
</constantSize>

<coalescentSimulator id="startingTree">
<taxa idref="taxa"/>
<constantSize idref="constant"/>
</coalescentSimulator>

	<treeModel id="treeModel">
		<coalescentTree idref="startingTree"/>
		<rootHeight>
			<parameter id="treeModel.rootHeight"/>
		</rootHeight>
		<nodeHeights internalNodes="true">
			<parameter id="treeModel.internalNodeHeights"/>
		</nodeHeights>
		<nodeHeights internalNodes="true" rootNode="true">
			<parameter id="treeModel.allInternalNodeHeights"/>
		</nodeHeights>
	</treeModel>

	<coalescentLikelihood id="coalescent">
		<model>
			<constantSize idref="constant"/>
		</model>
		<populationTree>
			<treeModel idref="treeModel"/>
		</populationTree>
	</coalescentLikelihood>

	<!-- The strict clock (Uniform rates across branches)                        -->
	<strictClockBranchRates id="branchRates">
		<rate>
			<parameter id="clock.rate" value="1.0" lower="0.0"/>
		</rate>
	</strictClockBranchRates>

	<gtrModel id="gtr">
		<frequencies>
			<frequencyModel dataType="nucleotide">
				<frequencies>
					<parameter id="frequencies" value="0.25 0.25 0.25 0.25"/>
				</frequencies>
			</frequencyModel>
		</frequencies>
		<rateAC>
			<parameter id="ac" value="1.0" lower="0.0"/>
		</rateAC>
		<rateAG>
			<parameter id="ag" value="1.0" lower="0.0"/>
		</rateAG>
		<rateAT>
			<parameter id="at" value="1.0" lower="0.0"/>
		</rateAT>
		<rateCG>
			<parameter id="cg" value="1.0" lower="0.0"/>
		</rateCG>
		<rateGT>
			<parameter id="gt" value="1.0" lower="0.0"/>
		</rateGT>
	</gtrModel>

	<siteModel id="siteModel">
		<substitutionModel>
			<gtrModel idref="gtr"/>
		</substitutionModel>
		<gammaShape gammaCategories="4">
			<parameter id="alpha" value="0.5" lower="0.0"/>
		</gammaShape>
	</siteModel>

	<treeLikelihood id="treeLikelihood" useAmbiguities="false">
		<patterns idref="patterns"/>
		<treeModel idref="treeModel"/>
		<siteModel idref="siteModel"/>
		<strictClockBranchRates idref="branchRates"/>
	</treeLikelihood>

	<operators id="operators" optimizationSchedule="default">
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="ac"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="ag"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="at"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="cg"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="gt"/>
		</scaleOperator>
		<deltaExchange delta="0.01" weight="0.1">
			<parameter idref="frequencies"/>
		</deltaExchange>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="alpha"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="3">
			<parameter idref="clock.rate"/>
		</scaleOperator>
		<subtreeSlide size="15.0" gaussian="true" weight="15">
			<treeModel idref="treeModel"/>
		</subtreeSlide>
		<narrowExchange weight="15">
			<treeModel idref="treeModel"/>
		</narrowExchange>
		<wideExchange weight="3">
			<treeModel idref="treeModel"/>
		</wideExchange>
		<wilsonBalding weight="3">
			<treeModel idref="treeModel"/>
		</wilsonBalding>
		<scaleOperator scaleFactor="0.75" weight="3">
			<parameter idref="treeModel.rootHeight"/>
		</scaleOperator>
		<uniformOperator weight="30">
			<parameter idref="treeModel.internalNodeHeights"/>
		</uniformOperator>
		<scaleOperator scaleFactor="0.75" weight="3">
			<parameter idref="constant.popSize"/>
		</scaleOperator>
		<upDownOperator scaleFactor="0.75" weight="3">
			<up>
				<parameter idref="clock.rate"/>
			</up>
			<down>
				<parameter idref="treeModel.allInternalNodeHeights"/>
			</down>
		</upDownOperator>
	</operators>

	<mcmc id="mcmc" chainLength="100000000" autoOptimize="true">
		<posterior id="posterior">
			<prior id="prior">
				<gammaPrior shape="0.05" scale="10.0" offset="0.0">
					<parameter idref="ac"/>
				</gammaPrior>
				<gammaPrior shape="0.05" scale="20.0" offset="0.0">
					<parameter idref="ag"/>
				</gammaPrior>
				<gammaPrior shape="0.05" scale="10.0" offset="0.0">
					<parameter idref="at"/>
				</gammaPrior>
				<gammaPrior shape="0.05" scale="10.0" offset="0.0">
					<parameter idref="cg"/>
				</gammaPrior>
				<gammaPrior shape="0.05" scale="10.0" offset="0.0">
					<parameter idref="gt"/>
				</gammaPrior>
				<uniformPrior lower="0.0" upper="1.0">
					<parameter idref="frequencies"/>
				</uniformPrior>
				<exponentialPrior mean="0.5" offset="0.0">
					<parameter idref="alpha"/>
				</exponentialPrior>
				<uniformPrior lower="0.0" upper="1.0">
					<parameter idref="clock.rate"/>
				</uniformPrior>
				<oneOnXPrior>
					<parameter idref="constant.popSize"/>
				</oneOnXPrior>
<coalescentLikelihood idref="coalescent"/>
</prior>
<likelihood id="likelihood">
<treeLikelihood idref="treeLikelihood"/>
</likelihood>
</posterior>
<operators idref="operators"/>

<log id="screenLog" logEvery="5000">
<column label="Posterior" dp="4" width="12">
<posterior idref="posterior"/>
</column>
<column label="Prior" dp="4" width="12">
<prior idref="prior"/>
</column>
<column label="Likelihood" dp="4" width="12">
<likelihood idref="likelihood"/>
</column>
<column label="rootHeight" sf="6" width="12">
<parameter idref="treeModel.rootHeight"/>
</column>
<column label="clock.rate" sf="6" width="12">
<parameter idref="clock.rate"/>
</column>
</log>

<log id="fileLog" logEvery="5000" fileName="FILENAME_strict_constant.log" overwrite="false">
<posterior idref="posterior"/>
<prior idref="prior"/>
<likelihood idref="likelihood"/>
<parameter idref="treeModel.rootHeight"/>
<parameter idref="constant.popSize"/>
<parameter idref="ac"/>
<parameter idref="ag"/>
<parameter idref="at"/>
<parameter idref="cg"/>
<parameter idref="gt"/>
<parameter idref="frequencies"/>
<parameter idref="alpha"/>
<parameter idref="clock.rate"/>
<treeLikelihood idref="treeLikelihood"/>
<coalescentLikelihood idref="coalescent"/>
</log>

<logTree id="treeFileLog" logEvery="5000" nexusFormat="true" fileName="FILENAME_strict_constant.trees" sortTranslationTable="true">
<treeModel idref="treeModel"/>
<trait name="rate" tag="rate">
<strictClockBranchRates idref="branchRates"/>
</trait>
<posterior idref="posterior"/>
</logTree>
</mcmc>

<marginalLikelihoodEstimator chainLength="10000000" pathSteps="100" pathScheme="betaquantile" alpha="0.3">
<samplers>
<mcmc idref="mcmc"/>
</samplers>
<pathLikelihood id="pathLikelihood">
<source>
<posterior idref="posterior"/>
</source>
<destination>
<prior idref="prior"/>
</destination>
</pathLikelihood>
<log id="MLELog" logEvery="1000" fileName="FILENAME_strict_constant.mle.log">
<pathLikelihood idref="pathLikelihood"/>
</log>
</marginalLikelihoodEstimator>

<pathSamplingAnalysis fileName="FILENAME_strict_constant.mle.log">
<likelihoodColumn name="pathLikelihood.delta"/>
<thetaColumn name="pathLikelihood.theta"/>
</pathSamplingAnalysis>

<steppingStoneSamplingAnalysis fileName="FILENAME_strict_constant.mle.log">
<likelihoodColumn name="pathLikelihood.delta"/>
<thetaColumn name="pathLikelihood.theta"/>
</steppingStoneSamplingAnalysis>

<report>
<property name="timer">
<mcmc idref="mcmc"/>
</property>
</report>
</beast>
'''

relaxed_constant = '''<?xml version="1.0" standalone="yes"?>
<beast>
  <taxa id="taxa">
TAXON_DEFINITION_BLOCK
</taxa>

<alignment id="alignment" dataType="nucleotide">
SEQUENCE_DEFINITION_BLOCK
</alignment>

	<patterns id="patterns" from="1" strip="false">
		<alignment idref="alignment"/>
	</patterns>

	<!-- A prior assumption that the population size has remained constant       -->
	<!-- throughout the time spanned by the genealogy.                           -->
	<constantSize id="constant" units="years">
		<populationSize>
			<parameter id="constant.popSize" value="150.0" lower="0.0"/>
		</populationSize>
	</constantSize>

	<!-- Generate a random starting tree under the coalescent process            -->
	<coalescentSimulator id="startingTree">
		<taxa idref="taxa"/>
		<constantSize idref="constant"/>
	</coalescentSimulator>

	<!-- Generate a tree model                                                   -->
	<treeModel id="treeModel">
		<coalescentTree idref="startingTree"/>
		<rootHeight>
			<parameter id="treeModel.rootHeight"/>
		</rootHeight>
		<nodeHeights internalNodes="true">
			<parameter id="treeModel.internalNodeHeights"/>
		</nodeHeights>
		<nodeHeights internalNodes="true" rootNode="true">
			<parameter id="treeModel.allInternalNodeHeights"/>
		</nodeHeights>
	</treeModel>

	<!-- Generate a coalescent likelihood                                        -->
	<coalescentLikelihood id="coalescent">
		<model>
			<constantSize idref="constant"/>
		</model>
		<populationTree>
			<treeModel idref="treeModel"/>
		</populationTree>
	</coalescentLikelihood>

	<!-- The uncorrelated relaxed clock (Drummond, Ho, Phillips & Rambaut (2006) PLoS Biology 4, e88 )-->
	<discretizedBranchRates id="branchRates">
		<treeModel idref="treeModel"/>
		<distribution>
			<logNormalDistributionModel meanInRealSpace="true">
				<mean>
					<parameter id="ucld.mean" value="0.05" lower="0.0"/>
				</mean>
				<stdev>
					<parameter id="ucld.stdev" value="0.3333333333333333" lower="0.0"/>
				</stdev>
			</logNormalDistributionModel>
		</distribution>
		<rateCategories>
			<parameter id="branchRates.categories"/>
		</rateCategories>
	</discretizedBranchRates>
	<rateStatistic id="meanRate" name="meanRate" mode="mean" internal="true" external="true">
		<treeModel idref="treeModel"/>
		<discretizedBranchRates idref="branchRates"/>
	</rateStatistic>
	<rateStatistic id="coefficientOfVariation" name="coefficientOfVariation" mode="coefficientOfVariation" internal="true" external="true">
		<treeModel idref="treeModel"/>
		<discretizedBranchRates idref="branchRates"/>
	</rateStatistic>
	<rateCovarianceStatistic id="covariance" name="covariance">
		<treeModel idref="treeModel"/>
		<discretizedBranchRates idref="branchRates"/>
	</rateCovarianceStatistic>

	<!-- The general time reversible (GTR) substitution model                    -->
	<gtrModel id="gtr">
		<frequencies>
			<frequencyModel dataType="nucleotide">
				<frequencies>
					<parameter id="frequencies" value="0.25 0.25 0.25 0.25"/>
				</frequencies>
			</frequencyModel>
		</frequencies>
		<rateAC>
			<parameter id="ac" value="1.0" lower="0.0"/>
		</rateAC>
		<rateAG>
			<parameter id="ag" value="1.0" lower="0.0"/>
		</rateAG>
		<rateAT>
			<parameter id="at" value="1.0" lower="0.0"/>
		</rateAT>
		<rateCG>
			<parameter id="cg" value="1.0" lower="0.0"/>
		</rateCG>
		<rateGT>
			<parameter id="gt" value="1.0" lower="0.0"/>
		</rateGT>
	</gtrModel>

	<!-- site model                                                              -->
	<siteModel id="siteModel">
		<substitutionModel>
			<gtrModel idref="gtr"/>
		</substitutionModel>
		<gammaShape gammaCategories="4">
			<parameter id="alpha" value="0.5" lower="0.0"/>
		</gammaShape>
	</siteModel>

	<!-- Likelihood for tree given sequence data                                 -->
	<treeLikelihood id="treeLikelihood" useAmbiguities="false">
		<patterns idref="patterns"/>
		<treeModel idref="treeModel"/>
		<siteModel idref="siteModel"/>
		<discretizedBranchRates idref="branchRates"/>
	</treeLikelihood>

	<!-- Define operators                                                        -->
	<operators id="operators" optimizationSchedule="default">
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="ac"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="ag"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="at"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="cg"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="gt"/>
		</scaleOperator>
		<deltaExchange delta="0.01" weight="0.1">
			<parameter idref="frequencies"/>
		</deltaExchange>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="alpha"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="3">
			<parameter idref="ucld.mean"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="3">
			<parameter idref="ucld.stdev"/>
		</scaleOperator>
		<subtreeSlide size="15.0" gaussian="true" weight="15">
			<treeModel idref="treeModel"/>
		</subtreeSlide>
		<narrowExchange weight="15">
			<treeModel idref="treeModel"/>
		</narrowExchange>
		<wideExchange weight="3">
			<treeModel idref="treeModel"/>
		</wideExchange>
		<wilsonBalding weight="3">
			<treeModel idref="treeModel"/>
		</wilsonBalding>
		<scaleOperator scaleFactor="0.75" weight="3">
			<parameter idref="treeModel.rootHeight"/>
		</scaleOperator>
		<uniformOperator weight="30">
			<parameter idref="treeModel.internalNodeHeights"/>
		</uniformOperator>
		<scaleOperator scaleFactor="0.75" weight="3">
			<parameter idref="constant.popSize"/>
		</scaleOperator>
		<upDownOperator scaleFactor="0.75" weight="3">
			<up>
				<parameter idref="ucld.mean"/>
			</up>
			<down>
				<parameter idref="treeModel.allInternalNodeHeights"/>
			</down>
		</upDownOperator>
		<swapOperator size="1" weight="10" autoOptimize="false">
			<parameter idref="branchRates.categories"/>
		</swapOperator>
		<uniformIntegerOperator weight="10">
			<parameter idref="branchRates.categories"/>
		</uniformIntegerOperator>
	</operators>

	<!-- Define MCMC                                                             -->
	<mcmc id="mcmc" chainLength="100000000" autoOptimize="true">
		<posterior id="posterior">
			<prior id="prior">
				<gammaPrior shape="0.05" scale="10.0" offset="0.0">
					<parameter idref="ac"/>
				</gammaPrior>
				<gammaPrior shape="0.05" scale="20.0" offset="0.0">
					<parameter idref="ag"/>
				</gammaPrior>
				<gammaPrior shape="0.05" scale="10.0" offset="0.0">
					<parameter idref="at"/>
				</gammaPrior>
				<gammaPrior shape="0.05" scale="10.0" offset="0.0">
					<parameter idref="cg"/>
				</gammaPrior>
				<gammaPrior shape="0.05" scale="10.0" offset="0.0">
					<parameter idref="gt"/>
				</gammaPrior>
				<uniformPrior lower="0.0" upper="1.0">
					<parameter idref="frequencies"/>
				</uniformPrior>
				<exponentialPrior mean="0.5" offset="0.0">
					<parameter idref="alpha"/>
				</exponentialPrior>
				<exponentialPrior mean="0.3333333333333333" offset="0.0">
					<parameter idref="ucld.stdev"/>
				</exponentialPrior>
				<uniformPrior lower="0.0" upper="10.0">
					<parameter idref="ucld.mean"/>
				</uniformPrior>
				<oneOnXPrior>
					<parameter idref="constant.popSize"/>
				</oneOnXPrior>
				<coalescentLikelihood idref="coalescent"/>
			</prior>
			<likelihood id="likelihood">
				<treeLikelihood idref="treeLikelihood"/>
			</likelihood>
		</posterior>
		<operators idref="operators"/>

		<!-- write log to screen                                                     -->
		<log id="screenLog" logEvery="5000">
			<column label="Posterior" dp="4" width="12">
				<posterior idref="posterior"/>
			</column>
			<column label="Prior" dp="4" width="12">
				<prior idref="prior"/>
			</column>
			<column label="Likelihood" dp="4" width="12">
				<likelihood idref="likelihood"/>
			</column>
			<column label="rootHeight" sf="6" width="12">
				<parameter idref="treeModel.rootHeight"/>
			</column>
			<column label="ucld.mean" sf="6" width="12">
				<parameter idref="ucld.mean"/>
			</column>
		</log>

		<!-- write log to file                                                       -->
		<log id="fileLog" logEvery="5000" fileName="FILENAME_ucld_constant.log" overwrite="false">
			<posterior idref="posterior"/>
			<prior idref="prior"/>
			<likelihood idref="likelihood"/>
			<parameter idref="treeModel.rootHeight"/>
			<parameter idref="constant.popSize"/>
			<parameter idref="ac"/>
			<parameter idref="ag"/>
			<parameter idref="at"/>
			<parameter idref="cg"/>
			<parameter idref="gt"/>
			<parameter idref="frequencies"/>
			<parameter idref="alpha"/>
			<parameter idref="ucld.mean"/>
			<parameter idref="ucld.stdev"/>
			<rateStatistic idref="meanRate"/>
			<rateStatistic idref="coefficientOfVariation"/>
			<rateCovarianceStatistic idref="covariance"/>
			<treeLikelihood idref="treeLikelihood"/>
			<coalescentLikelihood idref="coalescent"/>
		</log>

		<!-- write tree log to file                                                  -->
		<logTree id="treeFileLog" logEvery="5000" nexusFormat="true" fileName="FILENAME_ucld_constant.trees" sortTranslationTable="true">
			<treeModel idref="treeModel"/>
			<trait name="rate" tag="rate">
				<discretizedBranchRates idref="branchRates"/>
			</trait>
			<posterior idref="posterior"/>
		</logTree>
	</mcmc>

	<!-- START Marginal Likelihood Estimator                                     -->

	<!-- Define marginal likelihood estimator settings                           -->
	<marginalLikelihoodEstimator chainLength="10000000" pathSteps="100" pathScheme="betaquantile" alpha="0.3">
		<samplers>
			<mcmc idref="mcmc"/>
		</samplers>
		<pathLikelihood id="pathLikelihood">
			<source>
				<posterior idref="posterior"/>
			</source>
			<destination>
				<prior idref="prior"/>
			</destination>
		</pathLikelihood>
		<log id="MLELog" logEvery="1000" fileName="FILENAME_ucld_constant.mle.log">
			<pathLikelihood idref="pathLikelihood"/>
		</log>
	</marginalLikelihoodEstimator>

	<!-- Path sampling estimator from collected samples                          -->
	<pathSamplingAnalysis fileName="FILENAME_ucld_constant.mle.log">
		<likelihoodColumn name="pathLikelihood.delta"/>
		<thetaColumn name="pathLikelihood.theta"/>
	</pathSamplingAnalysis>

	<!-- Stepping-stone sampling estimator from collected samples                -->
	<steppingStoneSamplingAnalysis fileName="FILENAME_ucld_constant.mle.log">
		<likelihoodColumn name="pathLikelihood.delta"/>
		<thetaColumn name="pathLikelihood.theta"/>
	</steppingStoneSamplingAnalysis>

	<!-- END Marginal Likelihood Estimator                                       -->

	<report>
		<property name="timer">
			<mcmc idref="mcmc"/>
		</property>
	</report>
</beast>
'''


relaxed_skyline = '''<?xml version="1.0" standalone="yes"?>
<beast>
<taxa id="taxa">
TAXON_DEFINITION_BLOCK
</taxa>

<alignment id="alignment" dataType="nucleotide">
SEQUENCE_DEFINITION_BLOCK
</alignment>

	<!-- The unique patterns from 1 to end                                       -->
	<!-- npatterns=1186                                                          -->
	<patterns id="patterns" from="1" strip="false">
		<alignment idref="alignment"/>
	</patterns>

	<!-- This is a simple constant population size coalescent model              -->
	<!-- that is used to generate an initial tree for the chain.                 -->
	<constantSize id="initialDemo" units="years">
		<populationSize>
			<parameter id="initialDemo.popSize" value="100.0"/>
		</populationSize>
	</constantSize>

	<!-- Generate a random starting tree under the coalescent process            -->
	<coalescentSimulator id="startingTree">
		<taxa idref="taxa"/>
		<constantSize idref="initialDemo"/>
	</coalescentSimulator>

	<!-- Generate a tree model                                                   -->
	<treeModel id="treeModel">
		<coalescentTree idref="startingTree"/>
		<rootHeight>
			<parameter id="treeModel.rootHeight"/>
		</rootHeight>
		<nodeHeights internalNodes="true">
			<parameter id="treeModel.internalNodeHeights"/>
		</nodeHeights>
		<nodeHeights internalNodes="true" rootNode="true">
			<parameter id="treeModel.allInternalNodeHeights"/>
		</nodeHeights>
	</treeModel>

	<!-- Generate a generalizedSkyLineLikelihood for Bayesian Skyline            -->
	<generalizedSkyLineLikelihood id="skyline" linear="false">
		<populationSizes>
			<parameter id="skyline.popSize" dimension="10" value="150.0" lower="0.0"/>
		</populationSizes>
		<groupSizes>
			<parameter id="skyline.groupSize" dimension="10"/>
		</groupSizes>
		<populationTree>
			<treeModel idref="treeModel"/>
		</populationTree>
	</generalizedSkyLineLikelihood>
	<exponentialMarkovLikelihood id="eml1" jeffreys="true">
		<chainParameter>
			<parameter idref="skyline.popSize"/>
		</chainParameter>
	</exponentialMarkovLikelihood>

	<!-- The uncorrelated relaxed clock (Drummond, Ho, Phillips & Rambaut (2006) PLoS Biology 4, e88 )-->
	<discretizedBranchRates id="branchRates">
		<treeModel idref="treeModel"/>
		<distribution>
			<logNormalDistributionModel meanInRealSpace="true">
				<mean>
					<parameter id="ucld.mean" value="0.05" lower="0.0"/>
				</mean>
				<stdev>
					<parameter id="ucld.stdev" value="0.3333333333333333" lower="0.0"/>
				</stdev>
			</logNormalDistributionModel>
		</distribution>
		<rateCategories>
			<parameter id="branchRates.categories"/>
		</rateCategories>
	</discretizedBranchRates>
	<rateStatistic id="meanRate" name="meanRate" mode="mean" internal="true" external="true">
		<treeModel idref="treeModel"/>
		<discretizedBranchRates idref="branchRates"/>
	</rateStatistic>
	<rateStatistic id="coefficientOfVariation" name="coefficientOfVariation" mode="coefficientOfVariation" internal="true" external="true">
		<treeModel idref="treeModel"/>
		<discretizedBranchRates idref="branchRates"/>
	</rateStatistic>
	<rateCovarianceStatistic id="covariance" name="covariance">
		<treeModel idref="treeModel"/>
		<discretizedBranchRates idref="branchRates"/>
	</rateCovarianceStatistic>

	<!-- The general time reversible (GTR) substitution model                    -->
	<gtrModel id="gtr">
		<frequencies>
			<frequencyModel dataType="nucleotide">
				<frequencies>
					<parameter id="frequencies" value="0.25 0.25 0.25 0.25"/>
				</frequencies>
			</frequencyModel>
		</frequencies>
		<rateAC>
			<parameter id="ac" value="1.0" lower="0.0"/>
		</rateAC>
		<rateAG>
			<parameter id="ag" value="1.0" lower="0.0"/>
		</rateAG>
		<rateAT>
			<parameter id="at" value="1.0" lower="0.0"/>
		</rateAT>
		<rateCG>
			<parameter id="cg" value="1.0" lower="0.0"/>
		</rateCG>
		<rateGT>
			<parameter id="gt" value="1.0" lower="0.0"/>
		</rateGT>
	</gtrModel>

	<!-- site model                                                              -->
	<siteModel id="siteModel">
		<substitutionModel>
			<gtrModel idref="gtr"/>
		</substitutionModel>
		<gammaShape gammaCategories="4">
			<parameter id="alpha" value="0.5" lower="0.0"/>
		</gammaShape>
	</siteModel>

	<!-- Likelihood for tree given sequence data                                 -->
	<treeLikelihood id="treeLikelihood" useAmbiguities="false">
		<patterns idref="patterns"/>
		<treeModel idref="treeModel"/>
		<siteModel idref="siteModel"/>
		<discretizedBranchRates idref="branchRates"/>
	</treeLikelihood>

	<!-- Define operators                                                        -->
	<operators id="operators" optimizationSchedule="default">
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="ac"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="ag"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="at"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="cg"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="gt"/>
		</scaleOperator>
		<deltaExchange delta="0.01" weight="0.1">
			<parameter idref="frequencies"/>
		</deltaExchange>
		<scaleOperator scaleFactor="0.75" weight="0.1">
			<parameter idref="alpha"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="3">
			<parameter idref="ucld.mean"/>
		</scaleOperator>
		<scaleOperator scaleFactor="0.75" weight="3">
			<parameter idref="ucld.stdev"/>
		</scaleOperator>
		<subtreeSlide size="15.0" gaussian="true" weight="15">
			<treeModel idref="treeModel"/>
		</subtreeSlide>
		<narrowExchange weight="15">
			<treeModel idref="treeModel"/>
		</narrowExchange>
		<wideExchange weight="3">
			<treeModel idref="treeModel"/>
		</wideExchange>
		<wilsonBalding weight="3">
			<treeModel idref="treeModel"/>
		</wilsonBalding>
		<scaleOperator scaleFactor="0.75" weight="3">
			<parameter idref="treeModel.rootHeight"/>
		</scaleOperator>
		<uniformOperator weight="30">
			<parameter idref="treeModel.internalNodeHeights"/>
		</uniformOperator>
		<scaleOperator scaleFactor="0.75" weight="15">
			<parameter idref="skyline.popSize"/>
		</scaleOperator>
		<deltaExchange delta="1" integer="true" weight="6" autoOptimize="false">
			<parameter idref="skyline.groupSize"/>
		</deltaExchange>
		<upDownOperator scaleFactor="0.75" weight="3">
			<up>
				<parameter idref="ucld.mean"/>
			</up>
			<down>
				<parameter idref="treeModel.allInternalNodeHeights"/>
			</down>
		</upDownOperator>
		<swapOperator size="1" weight="10" autoOptimize="false">
			<parameter idref="branchRates.categories"/>
		</swapOperator>
		<uniformIntegerOperator weight="10">
			<parameter idref="branchRates.categories"/>
		</uniformIntegerOperator>
	</operators>

	<!-- Define MCMC                                                             -->
	<mcmc id="mcmc" chainLength="100000000" autoOptimize="true">
		<posterior id="posterior">
			<prior id="prior">
				<gammaPrior shape="0.05" scale="10.0" offset="0.0">
					<parameter idref="ac"/>
				</gammaPrior>
				<gammaPrior shape="0.05" scale="20.0" offset="0.0">
					<parameter idref="ag"/>
				</gammaPrior>
				<gammaPrior shape="0.05" scale="10.0" offset="0.0">
					<parameter idref="at"/>
				</gammaPrior>
				<gammaPrior shape="0.05" scale="10.0" offset="0.0">
					<parameter idref="cg"/>
				</gammaPrior>
				<gammaPrior shape="0.05" scale="10.0" offset="0.0">
					<parameter idref="gt"/>
				</gammaPrior>
				<uniformPrior lower="0.0" upper="1.0">
					<parameter idref="frequencies"/>
				</uniformPrior>
				<exponentialPrior mean="0.5" offset="0.0">
					<parameter idref="alpha"/>
				</exponentialPrior>
				<exponentialPrior mean="0.3333333333333333" offset="0.0">
					<parameter idref="ucld.stdev"/>
				</exponentialPrior>
				<uniformPrior lower="0.0" upper="10.0">
					<parameter idref="ucld.mean"/>
				</uniformPrior>
				<uniformPrior lower="0.0" upper="1.0E100">
					<parameter idref="skyline.popSize"/>
				</uniformPrior>
				<generalizedSkyLineLikelihood idref="skyline"/>
				<exponentialMarkovLikelihood idref="eml1"/>
			</prior>
			<likelihood id="likelihood">
				<treeLikelihood idref="treeLikelihood"/>
			</likelihood>
		</posterior>
		<operators idref="operators"/>

		<!-- write log to screen                                                     -->
		<log id="screenLog" logEvery="5000">
			<column label="Posterior" dp="4" width="12">
				<posterior idref="posterior"/>
			</column>
			<column label="Prior" dp="4" width="12">
				<prior idref="prior"/>
			</column>
			<column label="Likelihood" dp="4" width="12">
				<likelihood idref="likelihood"/>
			</column>
			<column label="rootHeight" sf="6" width="12">
				<parameter idref="treeModel.rootHeight"/>
			</column>
			<column label="ucld.mean" sf="6" width="12">
				<parameter idref="ucld.mean"/>
			</column>
		</log>

		<!-- write log to file                                                       -->
		<log id="fileLog" logEvery="5000" fileName="FILENAME_ucld_bs.log" overwrite="false">
			<posterior idref="posterior"/>
			<prior idref="prior"/>
			<likelihood idref="likelihood"/>
			<parameter idref="treeModel.rootHeight"/>
			<parameter idref="skyline.popSize"/>
			<parameter idref="skyline.groupSize"/>
			<parameter idref="ac"/>
			<parameter idref="ag"/>
			<parameter idref="at"/>
			<parameter idref="cg"/>
			<parameter idref="gt"/>
			<parameter idref="frequencies"/>
			<parameter idref="alpha"/>
			<parameter idref="ucld.mean"/>
			<parameter idref="ucld.stdev"/>
			<rateStatistic idref="meanRate"/>
			<rateStatistic idref="coefficientOfVariation"/>
			<rateCovarianceStatistic idref="covariance"/>
			<treeLikelihood idref="treeLikelihood"/>
			<generalizedSkyLineLikelihood idref="skyline"/>
		</log>

		<!-- write tree log to file                                                  -->
		<logTree id="treeFileLog" logEvery="5000" nexusFormat="true" fileName="FILENAME_ucld_bs.trees" sortTranslationTable="true">
			<treeModel idref="treeModel"/>
			<trait name="rate" tag="rate">
				<discretizedBranchRates idref="branchRates"/>
			</trait>
			<posterior idref="posterior"/>
		</logTree>
	</mcmc>

	<!-- START Marginal Likelihood Estimator                                     -->

	<!-- Define marginal likelihood estimator settings                           -->
	<marginalLikelihoodEstimator chainLength="10000000" pathSteps="100" pathScheme="betaquantile" alpha="0.3">
		<samplers>
			<mcmc idref="mcmc"/>
		</samplers>
		<pathLikelihood id="pathLikelihood">
			<source>
				<posterior idref="posterior"/>
			</source>
			<destination>
				<prior idref="prior"/>
			</destination>
		</pathLikelihood>
		<log id="MLELog" logEvery="1000" fileName="FILENAME_ucld_bs.mle.log">
			<pathLikelihood idref="pathLikelihood"/>
		</log>
	</marginalLikelihoodEstimator>

	<!-- Path sampling estimator from collected samples                          -->
	<pathSamplingAnalysis fileName="FILENAME_ucld_bs.mle.log">
		<likelihoodColumn name="pathLikelihood.delta"/>
		<thetaColumn name="pathLikelihood.theta"/>
	</pathSamplingAnalysis>

	<!-- Stepping-stone sampling estimator from collected samples                -->
	<steppingStoneSamplingAnalysis fileName="FILENAME_ucld_bs.mle.log">
		<likelihoodColumn name="pathLikelihood.delta"/>
		<thetaColumn name="pathLikelihood.theta"/>
	</steppingStoneSamplingAnalysis>

	<!-- END Marginal Likelihood Estimator                                       -->

	<report>
		<property name="timer">
			<mcmc idref="mcmc"/>
		</property>
	</report>
</beast>
'''






#Note that TAXONNAME CAN BE SPLIT TO FIND THE DATE


def parse_fasta(seq_file):
    seqdat = open(seq_file, 'r').readlines()
    seq_dict = {}
    
    for s in range(len(seqdat)):
        if '>' in seqdat[s]:
            seq_dict[re.sub('>| |\n', '', seqdat[s])] = seqdat[s+1]

    return seq_dict

def get_date(seq_name):
    date = re.findall('_([0-9]*[.]*[0-9]*)$', seq_name)[0]
    
    return date

def make_taxon_def_block(seq_dict):    
    template = '''
    <taxon id="T_NAME">
    <date value="T_DATE" direction="forwards" units="years"/>
    </taxon>
    '''
    taxon_block = list()
    for n in seq_dict:
        temp_block = re.sub('T_NAME', n, template)
        temp_date = get_date(n)
        temp_block = re.sub('T_DATE', temp_date, temp_block)
        taxon_block.append(temp_block)
    
    return ''.join(taxon_block)

def make_seq_def_block(seq_dict):
    template = '''
    <sequence>
    <taxon idref="T_NAME"/>
    T_SDATA
    </sequence>
    '''

    sequence_block = list()
    for n in seq_dict:
        temp_block = re.sub('T_NAME', n, template)
        temp_block = re.sub('T_SDATA', seq_dict[n], temp_block)
        sequence_block.append(temp_block)
    
    return ''.join(sequence_block)


############################
# Put it all together...
def make_xml(seq_data, model = 'sc', file_name = 'TEST_FILE'):

    if model == 'sc':
        template_xml = strict_constant
    elif model == 'ss':
        template_xml = strict_bs
    elif model == 'rc':
        template_xml = relaxed_constant
    elif model == 'rs':
        template_xml = relaxed_skyline
    else:
        raise Exception('Please specify a model of sc, bs, rc, or rs')

    t_block = make_taxon_def_block(seq_data)
    s_block = make_seq_def_block(seq_data)

    template_replace = re.sub('TAXON_DEFINITION_BLOCK', t_block, template_xml)
    template_replace = re.sub('SEQUENCE_DEFINITION_BLOCK', s_block, template_replace)
    template_replace = re.sub('FILENAME', file_name, template_replace)
    
    open(file_name+'.xml', 'w').write(template_replace)

    return template_replace


### parse everything through the command line
seq_data = parse_fasta(sys.argv[1])
template_name = re.sub('[.]fasta', '', sys.argv[1])

for i in ['sc', 'ss', 'rc', 'rs']:
    make_xml(seq_data, i, template_name+'_'+i)
    print 'wrote %s to %s' %(i, template_name+'_'+i+'.xml')


#print seq_data.keys()

##########
##########
#seq_data = parse_fasta('s_kentucky.fasta')
#strict_constant = make_xml(seq_data, 'sc', 'test_sc')
#strict_skyline = make_xml(seq_data, 'ss', 'test_ss')
#ucld_constant = make_xml(seq_data, 'rc', 'test_rc')
#ucld_skyline = make_xml(seq_data, 'rs', 'test_rs')
