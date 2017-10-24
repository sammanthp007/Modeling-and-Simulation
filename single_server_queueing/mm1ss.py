"""
External definitions for single-server queueing system.
Written by Samman Bikram Thapa @02755909
"""

import sys

# TODO: need these for successful running
"""
include "lcgrand.h"  /* Header file for random-number generator. */
void  report(void);
void  update_time_avg_stats(void);
float expon(float mean);
"""

class Simulate:
    def __init__():
        self.sim_time = 0.0
        self.server_status = 0
        self.total_of_delays = 0
        self.num_custs_delayed = 0
        self.time_arrival = []
        self.num_in_q = 0

        self.next_event_type = 0
        self.num_delays_required = 0
        self.num_events = 0
        self.area_num_in_q = 0.0
        self.area_server_status = 0.0
        self.mean_interarrival = 0.0
        self.mean_service = 0.0
        self.time_last_event = 0.0
        self.time_next_event = []


        self.Q_LIMIT = 100
        self.infile = 0
        self.outfile = 0

    def main(self):
        infile = open("mm1.in", "r")
        outfile = open("mm1/out", "w")
    
        # specify the number of events for timing function
        self.num_events = 2
    
        # Read input parameters
        inp = self.infile.readline()
        self.mean_interarrival, self.mean_service, self.num_delays_required = inp.split()
    
        # write report heading and input parameters
        self.outfile.write("Single-server Queueing System.\n\n")
        self.outfile.write("Mean interarrival time: ", self.mean_interarrival, "mins\n\n")
        self.outfile.write("Mean Service time: ", self.mean_service, "mins\n\n")
        self.outfile.write("Number of customers: ", self.num_delays_required, "\n\n")
    
        # initialize the simulation
        initialize()
    
        # run the simulation while more delays are still needed
        while self.num_custs_delayed < self.num_delays_required:
            # determine the next event
            timing()
    
            # update time-average statistical accumulators
            update_time_avg_stats()
    
            #invoke the appropriate event function
            if self.next_event_type == 1:
                arrive()
            else:
                depart()
    
        # invoke the report generator and end the simulation
        report()
    
        self.infile.close()
        self.outfile.close()
    
    
    
    # Arrive event function
    def arrive(self):
        delay = 0.0
        # schedule next arrival
        self.time_next_event[1] = self.sim_time + expon(self.mean_interarrival)
    
        # check to see whether server is busy
        if self.server_status == 1:
            # server is busy, so increment number if customers in  queue
            self.num_in_q += 1
    
            # check to see whether an overflow condition exists
            if self.num_in_q > self.Q_LIMIT:
                # Ovverflow, stop simulation
                print ("Overflow of customers at", self.sim_time)
                self.outfile.write("Overflow of customers at", self.sim_time)
                sys.exit()
    
            # no overflow, so store the time of arrival
            self.time_arrival[self.num_in_q] = self.sim_time;
        else:
            # no queue
            delay = 0.0
            self.total_of_delays += delay
    
            # increase the number of customers delayes
            # make server busy
            self.num_custs_delayed += 1
            self.server_status = 1
    
            # schedule a departure
            self.time_next_event[2] = self.sim_time + expon(self.mean_service)
    
    
    
    # Departure event function
    def depart(self):
        # two variables, i and delay
    
        # check to see whether the queue is empty
        if self.num_in_q == 0:
            # Queue is empty so make server idle and eliminate departure event
            # from consideration
            self.server_status = 0
            self.time_next_event[2] = 1.0 ** 30
        elif:
            # Queue is not empty, so decrement num of customers in queue
            self.num_in_q -= 1
    
            # Compute the delay of the customer who isbeginning service and
            # update total delay accumulator
            delay = sim_tim - self.time_arrival[1]
            self.total_of_delays += delay
    
            # increment the number of customer delayed
            # and schedule departure
            num_custs_delayes += 1
            self.time_next_event[2] = self.sim_time + expon(self.mean_service)

            # move each customer in queue up one place
            for i in range(1, self.num_in_q + 1):
                self.time_arrival[i] = self.time_arrival[i + 1]

    def initialize(self):
        # Initialize the simulation clock.
        self.sim_time = 0.0

        # initialize state variables
        self.server_status = 0
        self.num_in_q = 0
        self.time_last_event = 0.0

        # initialize statistical counters
        self.num_custs_delayed = 0
        self.total_of_delays = 0.0
        self.area_num_in_q = 0.0
        self.area_server_status = 0.0

        # init event list. Since no customers, departure (completiong) is eliminated
        self.time_next_event[1] = self.sim_time + expon(self.mean_interarrival)
        self.time_next_event[2] = 1 ** 30

    def timing(self):
        min_time_next_event = 1 ** 29

        self.next_event_type = 0

        # determine event type of next event to occur
        for i in range (self.num_events):
            if self.time_next_event[i] < min_time_next_event:
                min_time_next_event = self.time_next_event[i]
                self.next_event_type = 1

        # check to see whether the event list is empty
        if self.next_event_type == 0:
            # the event list is empty, so stop the simulation
            print ("Simulation completed at ", self.sim_time, "min")
            outfile.write("Simulation completed at ", self.sim_time, "min")
            sys.exit()

        # the event list is not empty, so advance the simulation clock
        self.sim_time = min_time_next_event




