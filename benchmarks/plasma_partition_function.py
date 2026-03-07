"""
Basic TARDIS Benchmark.
"""
import functools

from benchmarks.benchmark_base import BenchmarkBase
from tardis.plasma.properties.partition_function import (
    LevelBoltzmannFactorLTE,
    PartitionFunction,
)


class BenchmarkPartitionFunction(BenchmarkBase):
    """
    Class to benchmark partition function plasma properties.
    """

    repeat = 2

    @functools.cache
    def setup(self):
        self.sim = self.nb_simulation_verysimple

    def time_level_boltzmann_factor_lte(self):
        plasma = self.sim.plasma
        LevelBoltzmannFactorLTE.calculate(
            plasma.excitation_energy,
            plasma.g,
            plasma.beta_rad,
            plasma.levels,
        )

    def time_partition_function(self):
        plasma = self.sim.plasma
        PartitionFunction(plasma).calculate(plasma.level_boltzmann_factor)
