#
# Config file for SUMOS
#

# should use kafka for config changes (else it uses json file)
kafkaUpdates = True
# the kafka host we want to send our messages to
kafkaHost = "kafka:9092"

mqttUpdates = False
mqttHost = "localhost"
mqttPort = "1883"

# the topic we send the kafka messages to
kafkaTopicTrips = "crowd-nav-trips"
kafkaTopicPerformance = "crowd-nav-performance"
kafkaTopicRouting = "crowd-nav-routing"
kafkaTopicNis = "traffic"

# where we receive system changes
kafkaCommandsTopic = "crowd-nav-commands"
kafkaTlActionsTopic = "tl-actions"

# True if we want to use the SUMO GUI (always of in parallel mode)
sumoUseGUI = False  # False

# The network config (links to the net) we use for our simulation
sumoConfig = "./app/map/map.sumo.cfg"

# The network net we use for our simulation
sumoNet = "./app/map/map.net.xml"

# Initial wait time before publishing overheads
initialWaitTicks = 200

# the total number of cars we use in our simulation
totalCarCounter = 1000

# percentage of cars that are smart
smartCarPercentage = 0.2



# runtime dependent variable
processID = 0
parallelMode = False
