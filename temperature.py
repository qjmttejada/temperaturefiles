#Tejada, John Michael T. CPE41S2

from flask import Flask, jsonify, request

app = Flask(__name__)

# 1. Create a REST API using FLASK and insert a new temperature record to a JSON file. 
# The temperature information is composed of temp_id, date, and temperature.  (2 points)
temperatures = [

    {
        "temp_id" : 0,
        "date" : "09-28-2022",
        "temperature" : "32°C"
    },

    {
        "temp_id" : 1,
        "date" : "09-29-2022",
        "temperature" : "33°C"
    }

]

# 2, Create a REST API using FLASK to read temperature information from a JSON file. 
# The temperature information is composed of temp_id, date, and temperature.  (2 points)
@app.route('/temperatures', methods=['GET'])
def displayTemp():

    return jsonify(temperatures)

# 3. Create a REST API using FLASK to read the temperature information of a specific temperature id from a JSON file. 
# The temperature information is composed of temp_id, date, and temperature (2 points)
@app.route('/temperatures/<int:index>', methods=['GET'])
def displayById(indexd):

    return jsonify(temperatures[index])

# 4. Create a REST API using FLASK to update a temperature record of a specific temperature_id.  
# The temperature information is composed of temp_id, date, and temperature  (2 points)
@app.route('/temperatures', methods=['POST'])
def addTemp():

    temperature = request.get_json()
    temperatures.append(temperature)
    return {'id': len(temperatures)},200


# 5. Create a REST API using FLASK to delete a temperature record of a specific temperature_id. 
# The temperature information is composed of temp_id, date, and temperature   (2 points).
@app.route('/temperatures/<int:index>', methods=['DELETE'])
def deleteTempe(index):
    temperatures.pop(index)
    return 'Temperature was successfully deleted', 200

if __name__ == '__main__':

    app.run()