#!/usr/bin/env python3

import ea.ea_driver as ea_driver_class
import time
import util.args as args_class
import util.config as config_class


if __name__ == '__main__':

    # Process command line arguments
    args = args_class.Arguments(2, ['config/default.cfg', False])
    print(args.get_args())
    config_file, visualize = args.get_args() # Where visualize determines if
                                             # the best solution from this run
                                             # will be visualized
    
    visualize = bool(visualize)

    # Setup configuration
    config = config_class.Config(config_file)


    # Initialize the EA driver and its run variables
    ea_driver = ea_driver_class.EADriver(config)


    # Run the EA
    while ea_driver.run_count <= int(config.settings["num_experiment_runs"]):

        ea_driver.log.write_run_header(ea_driver.run_count)
        ea_driver.evaluate(ea_driver.population)

        sleep_count = 0

        while True:
            ea_driver.select_parents()

            ea_driver.recombine()

            ea_driver.mutate()

            ea_driver.evaluate(ea_driver.children)

            ea_driver.select_for_survival()

            if ea_driver.decide_termination():
                break

            if visualize:
                ea_driver.phenotype.visualize_pretty(ea_driver.best_fit_local_genotype.bulbs)
                if sleep_count <= 15:
                    time.sleep(1)
                    sleep_count += 1
            
        ea_driver.init_run_variables()
        ea_driver.increment_run_count()
