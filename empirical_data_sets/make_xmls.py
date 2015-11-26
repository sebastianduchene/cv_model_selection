import re, sys, os

strict_constant = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?><beast beautitemplate='Standard' beautistatus='' namespace="beast.core:beast.evolution.alignment:beast.evolution.tree.coalescent:beast.core.util:beast.evolution.nuc:beast.evolution.operators:beast.evolution.sitemodel:beast.evolution.substitutionmodel:beast.evolution.likelihood" version="2.0">


    <data
id="alignment"
name="alignment">
SEQUENCE_DEFINITION_BLOCK
</data>

<map name="Uniform">beast.math.distributions.Uniform</map>
<map name="Exponential">beast.math.distributions.Exponential</map>
<map name="LogNormal">beast.math.distributions.LogNormalDistributionModel</map>
<map name="Normal">beast.math.distributions.Normal</map>
<map name="Beta">beast.math.distributions.Beta</map>
<map name="Gamma">beast.math.distributions.Gamma</map>
<map name="LaplaceDistribution">beast.math.distributions.LaplaceDistribution</map>
<map name="prior">beast.math.distributions.Prior</map>
<map name="InverseGamma">beast.math.distributions.InverseGamma</map>
<map name="OneOnX">beast.math.distributions.OneOnX</map>

<run id="mcmc" spec="MCMC" chainLength="10000000">
    <state id="state" storeEvery="5000">

        <tree id="Tree.t:alignment" name="stateNode">
            <trait id="dateTrait.t:alignment" spec="beast.evolution.tree.TraitSet" traitname="date">
SEQUENCE_DATES_BLOCK
<taxa id="TaxonSet.alignment" spec="TaxonSet">
                <alignment idref="alignment"/>
</taxa>
</trait>
 <taxonset idref="TaxonSet.alignment"/>

        </tree>

        <parameter id="freqParameter.s:alignment" dimension="4" lower="0.0" name="stateNode" upper="1.0">0.25</parameter>
        <parameter id="rateAC.s:alignment" lower="0.0" name="stateNode">1.0</parameter>
        <parameter id="rateAG.s:alignment" lower="0.0" name="stateNode">1.0</parameter>
        <parameter id="rateAT.s:alignment" lower="0.0" name="stateNode">1.0</parameter>
        <parameter id="rateCG.s:alignment" lower="0.0" name="stateNode">1.0</parameter>
        <parameter id="rateGT.s:alignment" lower="0.0" name="stateNode">1.0</parameter>
        <parameter id="gammaShape.s:alignment" name="stateNode">1.0</parameter>
        <parameter id="popSize.t:alignment" name="stateNode">0.3</parameter>
    </state>

    <init id="RandomTree.t:alignment" spec="beast.evolution.tree.RandomTree" estimate="false" initial="@Tree.t:alignment" taxa="@alignment">
        <populationModel id="ConstantPopulation0.t:alignment" spec="ConstantPopulation">
            <parameter id="randomPopSize.t:alignment" name="popSize">1.0</parameter>
        </populationModel>
    </init>

    <distribution id="posterior" spec="util.CompoundDistribution">
        <distribution id="prior" spec="util.CompoundDistribution">
            <distribution id="CoalescentConstant.t:alignment" spec="Coalescent">
                <populationModel id="ConstantPopulation.t:alignment" spec="ConstantPopulation" popSize="@popSize.t:alignment"/>
                <treeIntervals id="TreeIntervals.t:alignment" spec="TreeIntervals" tree="@Tree.t:alignment"/>
            </distribution>
            <prior id="GammaShapePrior.s:alignment" name="distribution" x="@gammaShape.s:alignment">
                <Exponential id="Exponential.0" name="distr">
                    <parameter id="RealParameter.0" lower="0.0" name="mean" upper="0.0">1.0</parameter>
                </Exponential>
            </prior>
            <prior id="PopSizePrior.t:alignment" name="distribution" x="@popSize.t:alignment">
                <OneOnX id="OneOnX.0" name="distr"/>
            </prior>
            <prior id="RateACPrior.s:alignment" name="distribution" x="@rateAC.s:alignment">
                <Gamma id="Gamma.0" name="distr">
                    <parameter id="RealParameter.01" estimate="false" name="alpha">0.05</parameter>
                    <parameter id="RealParameter.02" estimate="false" name="beta">10.0</parameter>
                </Gamma>
            </prior>
            <prior id="RateAGPrior.s:alignment" name="distribution" x="@rateAG.s:alignment">
                <Gamma id="Gamma.01" name="distr">
                    <parameter id="RealParameter.03" estimate="false" name="alpha">0.05</parameter>
                    <parameter id="RealParameter.04" estimate="false" name="beta">20.0</parameter>
                </Gamma>
            </prior>
            <prior id="RateATPrior.s:alignment" name="distribution" x="@rateAT.s:alignment">
                <Gamma id="Gamma.02" name="distr">
                    <parameter id="RealParameter.05" estimate="false" name="alpha">0.05</parameter>
                    <parameter id="RealParameter.06" estimate="false" name="beta">10.0</parameter>
                </Gamma>
            </prior>
            <prior id="RateCGPrior.s:alignment" name="distribution" x="@rateCG.s:alignment">
                <Gamma id="Gamma.03" name="distr">
                    <parameter id="RealParameter.07" estimate="false" name="alpha">0.05</parameter>
                    <parameter id="RealParameter.08" estimate="false" name="beta">10.0</parameter>
                </Gamma>
            </prior>
            <prior id="RateGTPrior.s:alignment" name="distribution" x="@rateGT.s:alignment">
                <Gamma id="Gamma.04" name="distr">
                    <parameter id="RealParameter.09" estimate="false" name="alpha">0.05</parameter>
                    <parameter id="RealParameter.010" estimate="false" name="beta">10.0</parameter>
                </Gamma>
            </prior>
        </distribution>

        <distribution id="likelihood" spec="util.CompoundDistribution">
            <distribution id="treeLikelihood.alignment" spec="TreeLikelihood" data="@alignment" tree="@Tree.t:alignment">
                <siteModel id="SiteModel.s:alignment" spec="SiteModel" gammaCategoryCount="4" shape="@gammaShape.s:alignment">
                    <parameter id="mutationRate.s:alignment" estimate="false" name="mutationRate">1.0</parameter>
                    <parameter id="proportionInvariant.s:alignment" estimate="false" lower="0.0" name="proportionInvariant" upper="1.0">0.0</parameter>
                    <substModel id="gtr.s:alignment" spec="GTR" rateAC="@rateAC.s:alignment" rateAG="@rateAG.s:alignment" rateAT="@rateAT.s:alignment" rateCG="@rateCG.s:alignment" rateGT="@rateGT.s:alignment">
                        <parameter id="rateCT.s:alignment" estimate="false" lower="0.0" name="rateCT">1.0</parameter>
                        <frequencies id="estimatedFreqs.s:alignment" spec="Frequencies" frequencies="@freqParameter.s:alignment"/>
                    </substModel>
                </siteModel>
                <branchRateModel id="StrictClock.c:alignment" spec="beast.evolution.branchratemodel.StrictClockModel">
                    <parameter id="clockRate.c:alignment" estimate="false" name="clock.rate">1.0</parameter>
                </branchRateModel>
            </distribution>
        </distribution>
    </distribution>

    <operator id="treeScaler.t:alignment" spec="ScaleOperator" scaleFactor="0.5" tree="@Tree.t:alignment" weight="3.0"/>
    <operator id="treeRootScaler.t:alignment" spec="ScaleOperator" rootOnly="true" scaleFactor="0.5" tree="@Tree.t:alignment" weight="3.0"/>
    <operator id="UniformOperator.t:alignment" spec="Uniform" tree="@Tree.t:alignment" weight="30.0"/>
    <operator id="SubtreeSlide.t:alignment" spec="SubtreeSlide" tree="@Tree.t:alignment" weight="15.0"/>
    <operator id="narrow.t:alignment" spec="Exchange" tree="@Tree.t:alignment" weight="15.0"/>
    <operator id="wide.t:alignment" spec="Exchange" isNarrow="false" tree="@Tree.t:alignment" weight="3.0"/>
    <operator id="WilsonBalding.t:alignment" spec="WilsonBalding" tree="@Tree.t:alignment" weight="3.0"/>

    <operator id="FrequenciesExchanger.s:alignment" spec="DeltaExchangeOperator" delta="0.01" weight="0.1">
        <parameter idref="freqParameter.s:alignment"/>
    </operator>

    <operator id="RateACScaler.s:alignment" spec="ScaleOperator" parameter="@rateAC.s:alignment" scaleFactor="0.5" weight="0.1"/>
    <operator id="RateAGScaler.s:alignment" spec="ScaleOperator" parameter="@rateAG.s:alignment" scaleFactor="0.5" weight="0.1"/>
    <operator id="RateATScaler.s:alignment" spec="ScaleOperator" parameter="@rateAT.s:alignment" scaleFactor="0.5" weight="0.1"/>
    <operator id="RateCGScaler.s:alignment" spec="ScaleOperator" parameter="@rateCG.s:alignment" scaleFactor="0.5" weight="0.1"/>
    <operator id="RateGTScaler.s:alignment" spec="ScaleOperator" parameter="@rateGT.s:alignment" scaleFactor="0.5" weight="0.1"/>
    <operator id="gammaShapeScaler.s:alignment" spec="ScaleOperator" parameter="@gammaShape.s:alignment" scaleFactor="0.5" weight="0.1"/>
    <operator id="PopSizeScaler.t:alignment" spec="ScaleOperator" parameter="@popSize.t:alignment" scaleFactor="0.75" weight="3.0"/>

    <logger id="tracelog" fileName="FILE_NAME.log" logEvery="1000" model="@posterior" sanitiseHeaders="true" sort="smart">
        <log idref="posterior"/>
        <log idref="likelihood"/>
        <log idref="prior"/>
        <log idref="treeLikelihood.alignment"/>
        <log id="TreeHeight.t:alignment" spec="beast.evolution.tree.TreeHeightLogger" tree="@Tree.t:alignment"/>
        <log idref="freqParameter.s:alignment"/>
        <log idref="rateAC.s:alignment"/>
        <log idref="rateAG.s:alignment"/>
        <log idref="rateAT.s:alignment"/>
        <log idref="rateCG.s:alignment"/>
        <log idref="rateGT.s:alignment"/>
        <log idref="gammaShape.s:alignment"/>
        <log idref="popSize.t:alignment"/>
        <log idref="CoalescentConstant.t:alignment"/>
    </logger>

    <logger id="screenlog" logEvery="1000">
        <log idref="posterior"/>
        <log id="ESS.0" spec="util.ESS" arg="@posterior"/>
        <log idref="likelihood"/>
        <log idref="prior"/>
    </logger>

    <logger id="treelog.t:alignment" fileName="FILE_NAME.trees" logEvery="1000" mode="tree">
        <log id="TreeWithMetaDataLogger.t:alignment" spec="beast.evolution.tree.TreeWithMetaDataLogger" tree="@Tree.t:alignment"/>
    </logger>

</run>

</beast>
'''



strict_exponential = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?><beast beautitemplate='Standard' beautistatus='' namespace="beast.core:beast.evolution.alignment:beast.evolution.tree.coalescent:beast.core.util:beast.evolution.nuc:beast.evolution.operators:beast.evolution.sitemodel:beast.evolution.substitutionmodel:beast.evolution.likelihood" version="2.0">


    <data
id="alignment"
name="alignment">
SEQUENCE_DEFINITION_BLOCK
</data>

<map name="Uniform">beast.math.distributions.Uniform</map>
<map name="Exponential">beast.math.distributions.Exponential</map>
<map name="LogNormal">beast.math.distributions.LogNormalDistributionModel</map>
<map name="Normal">beast.math.distributions.Normal</map>
<map name="Beta">beast.math.distributions.Beta</map>
<map name="Gamma">beast.math.distributions.Gamma</map>
<map name="LaplaceDistribution">beast.math.distributions.LaplaceDistribution</map>
<map name="prior">beast.math.distributions.Prior</map>
<map name="InverseGamma">beast.math.distributions.InverseGamma</map>
<map name="OneOnX">beast.math.distributions.OneOnX</map>

<run id="mcmc" spec="MCMC" chainLength="10000000">
    <state id="state" storeEvery="5000">

        <tree id="Tree.t:alignment" name="stateNode">
            <trait id="dateTrait.t:alignment" spec="beast.evolution.tree.TraitSet" traitname="date">
SEQUENCE_DATES_BLOCK
<taxa id="TaxonSet.alignment" spec="TaxonSet">
                <alignment idref="alignment"/>
</taxa>
</trait>
 <taxonset idref="TaxonSet.alignment"/>

        </tree>

        <parameter id="freqParameter.s:alignment" dimension="4" lower="0.0" name="stateNode" upper="1.0">0.25</parameter>
        <parameter id="rateAC.s:alignment" lower="0.0" name="stateNode">1.0</parameter>
        <parameter id="rateAG.s:alignment" lower="0.0" name="stateNode">1.0</parameter>
        <parameter id="rateAT.s:alignment" lower="0.0" name="stateNode">1.0</parameter>
        <parameter id="rateCG.s:alignment" lower="0.0" name="stateNode">1.0</parameter>
        <parameter id="rateGT.s:alignment" lower="0.0" name="stateNode">1.0</parameter>
        <parameter id="gammaShape.s:alignment" name="stateNode">1.0</parameter>
        <parameter id="ePopSize.t:alignment" name="stateNode">0.3</parameter>
        <parameter id="growthRate.t:alignment" name="stateNode">3.0E-4</parameter>

    </state>

    <init id="RandomTree.t:alignment" spec="beast.evolution.tree.RandomTree" estimate="false" initial="@Tree.t:alignment" taxa="@alignment">
        <populationModel id="ConstantPopulation0.t:alignment" spec="ConstantPopulation">
            <parameter id="randomPopSize.t:alignment" name="popSize">1.0</parameter>
        </populationModel>
    </init>

    <distribution id="posterior" spec="util.CompoundDistribution">
        <distribution id="prior" spec="util.CompoundDistribution">

            <distribution id="CoalescentExponential.t:alignment" spec="Coalescent">
                <populationModel id="ExponentialGrowth.t:alignment" spec="ExponentialGrowth" growthRate="@growthRate.t:alignment" popSize="@ePopSize.t:alignment"/>
                <treeIntervals id="TreeIntervals.t:alignment" spec="TreeIntervals" tree="@Tree.t:alignment"/>
            </distribution>



            <prior id="GammaShapePrior.s:alignment" name="distribution" x="@gammaShape.s:alignment">
                <Exponential id="Exponential.0" name="distr">
                    <parameter id="RealParameter.0" lower="0.0" name="mean" upper="0.0">1.0</parameter>
                </Exponential>
            </prior>
            <prior id="ePopSizePrior.t:alignment" name="distribution" x="@ePopSize.t:alignment">
                <OneOnX id="OneOnX.0" name="distr"/>
            </prior>
            <prior id="GrowthRatePrior.t:alignment" name="distribution" x="@growthRate.t:alignment">
                <LaplaceDistribution id="LaplaceDistribution.0" name="distr">
                    <parameter id="RealParameter.001" estimate="false" name="mu">0.001</parameter>
                    <parameter id="RealParameter.002" estimate="false" name="scale">30.701135</parameter>
                </LaplaceDistribution>
            </prior>

            <prior id="RateACPrior.s:alignment" name="distribution" x="@rateAC.s:alignment">
                <Gamma id="Gamma.0" name="distr">
                    <parameter id="RealParameter.01" estimate="false" name="alpha">0.05</parameter>
                    <parameter id="RealParameter.02" estimate="false" name="beta">10.0</parameter>
                </Gamma>
            </prior>
            <prior id="RateAGPrior.s:alignment" name="distribution" x="@rateAG.s:alignment">
                <Gamma id="Gamma.01" name="distr">
                    <parameter id="RealParameter.03" estimate="false" name="alpha">0.05</parameter>
                    <parameter id="RealParameter.04" estimate="false" name="beta">20.0</parameter>
                </Gamma>
            </prior>
            <prior id="RateATPrior.s:alignment" name="distribution" x="@rateAT.s:alignment">
                <Gamma id="Gamma.02" name="distr">
                    <parameter id="RealParameter.05" estimate="false" name="alpha">0.05</parameter>
                    <parameter id="RealParameter.06" estimate="false" name="beta">10.0</parameter>
                </Gamma>
            </prior>
            <prior id="RateCGPrior.s:alignment" name="distribution" x="@rateCG.s:alignment">
                <Gamma id="Gamma.03" name="distr">
                    <parameter id="RealParameter.07" estimate="false" name="alpha">0.05</parameter>
                    <parameter id="RealParameter.08" estimate="false" name="beta">10.0</parameter>
                </Gamma>
            </prior>
            <prior id="RateGTPrior.s:alignment" name="distribution" x="@rateGT.s:alignment">
                <Gamma id="Gamma.04" name="distr">
                    <parameter id="RealParameter.09" estimate="false" name="alpha">0.05</parameter>
                    <parameter id="RealParameter.010" estimate="false" name="beta">10.0</parameter>
                </Gamma>
            </prior>
        </distribution>

        <distribution id="likelihood" spec="util.CompoundDistribution">
            <distribution id="treeLikelihood.alignment" spec="TreeLikelihood" data="@alignment" tree="@Tree.t:alignment">
                <siteModel id="SiteModel.s:alignment" spec="SiteModel" gammaCategoryCount="4" shape="@gammaShape.s:alignment">
                    <parameter id="mutationRate.s:alignment" estimate="false" name="mutationRate">1.0</parameter>
                    <parameter id="proportionInvariant.s:alignment" estimate="false" lower="0.0" name="proportionInvariant" upper="1.0">0.0</parameter>
                    <substModel id="gtr.s:alignment" spec="GTR" rateAC="@rateAC.s:alignment" rateAG="@rateAG.s:alignment" rateAT="@rateAT.s:alignment" rateCG="@rateCG.s:alignment" rateGT="@rateGT.s:alignment">
                        <parameter id="rateCT.s:alignment" estimate="false" lower="0.0" name="rateCT">1.0</parameter>
                        <frequencies id="estimatedFreqs.s:alignment" spec="Frequencies" frequencies="@freqParameter.s:alignment"/>
                    </substModel>
                </siteModel>
                <branchRateModel id="StrictClock.c:alignment" spec="beast.evolution.branchratemodel.StrictClockModel">
                    <parameter id="clockRate.c:alignment" estimate="false" name="clock.rate">1.0</parameter>
                </branchRateModel>
            </distribution>
        </distribution>
    </distribution>

    <operator id="treeScaler.t:alignment" spec="ScaleOperator" scaleFactor="0.5" tree="@Tree.t:alignment" weight="3.0"/>
    <operator id="treeRootScaler.t:alignment" spec="ScaleOperator" rootOnly="true" scaleFactor="0.5" tree="@Tree.t:alignment" weight="3.0"/>
    <operator id="UniformOperator.t:alignment" spec="Uniform" tree="@Tree.t:alignment" weight="30.0"/>
    <operator id="SubtreeSlide.t:alignment" spec="SubtreeSlide" tree="@Tree.t:alignment" weight="15.0"/>
    <operator id="narrow.t:alignment" spec="Exchange" tree="@Tree.t:alignment" weight="15.0"/>
    <operator id="wide.t:alignment" spec="Exchange" isNarrow="false" tree="@Tree.t:alignment" weight="3.0"/>
    <operator id="WilsonBalding.t:alignment" spec="WilsonBalding" tree="@Tree.t:alignment" weight="3.0"/>

    <operator id="FrequenciesExchanger.s:alignment" spec="DeltaExchangeOperator" delta="0.01" weight="0.1">
        <parameter idref="freqParameter.s:alignment"/>
    </operator>

    <operator id="RateACScaler.s:alignment" spec="ScaleOperator" parameter="@rateAC.s:alignment" scaleFactor="0.5" weight="0.1"/>
    <operator id="RateAGScaler.s:alignment" spec="ScaleOperator" parameter="@rateAG.s:alignment" scaleFactor="0.5" weight="0.1"/>
    <operator id="RateATScaler.s:alignment" spec="ScaleOperator" parameter="@rateAT.s:alignment" scaleFactor="0.5" weight="0.1"/>
    <operator id="RateCGScaler.s:alignment" spec="ScaleOperator" parameter="@rateCG.s:alignment" scaleFactor="0.5" weight="0.1"/>
    <operator id="RateGTScaler.s:alignment" spec="ScaleOperator" parameter="@rateGT.s:alignment" scaleFactor="0.5" weight="0.1"/>
    <operator id="gammaShapeScaler.s:alignment" spec="ScaleOperator" parameter="@gammaShape.s:alignment" scaleFactor="0.5" weight="0.1"/>
    <operator id="ePopSizeScaler.t:alignment" spec="ScaleOperator" parameter="@ePopSize.t:alignment" scaleFactor="0.75" weight="3.0"/>
    <operator id="GrowthRateRandomWalk.t:alignment" spec="RealRandomWalkOperator" parameter="@growthRate.t:alignment" weight="3.0" windowSize="1.0"/>

    <logger id="tracelog" fileName="FILE_NAME.log" logEvery="1000" model="@posterior" sanitiseHeaders="true" sort="smart">
        <log idref="posterior"/>
        <log idref="likelihood"/>
        <log idref="prior"/>
        <log idref="treeLikelihood.alignment"/>
        <log id="TreeHeight.t:alignment" spec="beast.evolution.tree.TreeHeightLogger" tree="@Tree.t:alignment"/>
        <log idref="freqParameter.s:alignment"/>
        <log idref="rateAC.s:alignment"/>
        <log idref="rateAG.s:alignment"/>
        <log idref="rateAT.s:alignment"/>
        <log idref="rateCG.s:alignment"/>
        <log idref="rateGT.s:alignment"/>
        <log idref="gammaShape.s:alignment"/>
        <log idref="CoalescentExponential.t:alignment"/>
        <log idref="ePopSize.t:alignment"/>
        <log idref="growthRate.t:alignment"/>

    </logger>

    <logger id="screenlog" logEvery="1000">
        <log idref="posterior"/>
        <log id="ESS.0" spec="util.ESS" arg="@posterior"/>
        <log idref="likelihood"/>
        <log idref="prior"/>
    </logger>

    <logger id="treelog.t:alignment" fileName="FILE_NAME.trees" logEvery="1000" mode="tree">
        <log id="TreeWithMetaDataLogger.t:alignment" spec="beast.evolution.tree.TreeWithMetaDataLogger" tree="@Tree.t:alignment"/>
    </logger>

</run>

</beast>
'''




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


def make_sequence_block(seq_input):
    block_temp = []
    seq_template = '<sequence id="TAXON_NAME" taxon="TAXON_NAME" totalcount="4" value="SEQUENCE"/>'
    for n in seq_input:
        sub_1 = re.sub('TAXON_NAME', n, seq_template)
        sub_2 = re.sub('SEQUENCE', seq_input[n], sub_1)
        sub_3 = re.sub('\n', '', sub_2)
        block_temp.append(sub_3)
    return '\n'.join(block_temp)

def make_dates_block(seq_input):
    block_temp = []
    for n in seq_input:
        block_temp.append(n+'='+get_date(n))
    return ',\n'.join(block_temp)




def make_strict_constant(seq_input, out_name):
    sequences = make_sequence_block(seq_input)
    dates = make_dates_block(seq_input)
    s1 = re.sub('SEQUENCE_DEFINITION_BLOCK', sequences, strict_constant)
    s2 = re.sub('SEQUENCE_DATES_BLOCK', dates, s1)
    s3 = re.sub('FILE_NAME', out_name, s2)
    return s3


def make_strict_exponential(seq_input, out_name):
    sequences = make_sequence_block(seq_input)
    dates = make_dates_block(seq_input)
    s1 = re.sub('SEQUENCE_DEFINITION_BLOCK', sequences, strict_exponential)
    s2 = re.sub('SEQUENCE_DATES_BLOCK', dates, s1)
    s3 = re.sub('FILE_NAME', out_name, s2)
    return s3




