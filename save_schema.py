from owmeta_core.command import OWM
from owmeta.data_trans.wormbase import (MuscleWormBaseCSVTranslator, WormBaseCSVDataSource,
                                        WormbaseIonChannelCSVDataSource, WormbaseIonChannelCSVTranslator)
from owmeta.data_trans.neuron_data import NeuronCSVDataSource, NeuronCSVDataTranslator


owm = OWM()

for module in ('owmeta.neuron',
               'owmeta.worm',
               'owmeta.biology',
               'owmeta.cell',
               'owmeta.channel',
               'owmeta.channelworm',
               'owmeta.connection',
               'owmeta.document',
               'owmeta.evidence',
               'owmeta.experiment',
               'owmeta.muscle',
               'owmeta.network',
               'owmeta.plot',
               'owmeta.website',
               'owmeta.data_trans.bibtex',
               'owmeta.data_trans.connections',
               'owmeta.data_trans.context_merge',
               'owmeta.data_trans.data_with_evidence_ds',
               'owmeta.data_trans.neuron_data',
               'owmeta.data_trans.wormatlas',
               'owmeta.data_trans.wormbase',
               'owmeta.sources',
               'owmeta.translators',
               ):
    owm.save(module)

# We don't have to use the URIs for sources here since we're recreating the
ctx = owm.default_context.stored
muscles = owm.translate(MuscleWormBaseCSVTranslator(),
        data_sources=(WormBaseCSVDataSource(key='wormbase_celegans_cells'),),
        output_key='muscles')
ctx(muscles).description(
        "Contains descriptions of C. elegans muscles and is the"
        " principle such list for OpenWorm")

neurons = owm.translate(NeuronCSVDataTranslator(),
        data_sources=(NeuronCSVDataSource(key='neurons'),),
        output_key='neurons')
ctx(neurons).description(
        "Contains descriptions of C. elegans neurons and is the"
        " principle such list for OpenWorm")

ion_channels = owm.translate(
        WormbaseIonChannelCSVTranslator(),
        data_sources=(WormbaseIonChannelCSVDataSource(key='ion_channels'),),
        output_key='ion_channels')
ctx(ion_channels).description(
        "Contains Channels and ExpressionPatterns")

ctx.save()
