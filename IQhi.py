from numpy import *
import numpy as np
import pandas as pd


headers = ['R1 (Ohm)', 'R2 (Ohm)', 'R3 (Ohm)']


def csv2txt(file_name):
    class NeuralNet(object):
        def __init__(self):
            random.seed(1)
            self.synaptic_weights = 2 * random.random((3, 3)) - 1

        def __ReLU(self, x):
            return np.where(x < 0, 0, x)

        def __ReLU_derivative(self, x):
            return np.where(x < 0, 0, 1)

        def train(self, inputs, outputs, training_iterations):
            for iteration in range(training_iterations):
                output = self.learn(inputs)
                error = outputs - output
                factor = dot(inputs.T, error * self.__ReLU_derivative(output))
                self.synaptic_weights += factor

        def learn(self, inputs):
            return self.__ReLU(dot(inputs, self.synaptic_weights))

    neural_network = NeuralNet()
    raw_a = []
    raw_b = []
    raw_c = []
    temp_inputs = []
    temp_outputs = []
    csv_file_name = "/Users/xichao/Desktop/fitting data/" + file_name + ".csv"
    first_in = pd.read_csv(csv_file_name)
    element = pd.DataFrame(first_in, columns=headers)
    products_list = element.values.tolist()
    for data_set in products_list:
        raw_a.append(data_set[0])
        raw_b.append(data_set[1])
        raw_c.append(data_set[2])
    for i in range(4):
        raw_a.pop()
        raw_b.pop()
        raw_c.pop()

    raw_elem = [list(x) for x in zip(raw_a, raw_b, raw_c)]
    real_data = raw_elem.pop()
    test_case = raw_elem.pop()
    if len(raw_elem) % 3 != 0:
        if len(raw_elem) % 3 == 1:
            raw_elem.pop()
        if len(raw_elem) % 3 == 2:
            raw_elem.pop()
            raw_elem.pop()
    print(len(raw_elem))
    counter = 0
    for i in range(len(raw_elem)):
        if counter == 0:
            temp_inputs.append(raw_elem[i])
            counter += 1
        elif counter == 1:
            temp_inputs.append(raw_elem[i])
            temp_outputs.append(raw_elem[i])
            counter += 1
        elif counter == 2:
            temp_outputs.append(raw_elem[i])
            counter = 0
    inputs = array(temp_inputs)
    outputs = array(temp_outputs)
    list_container = []
    neural_network.train(inputs, outputs, 1000000)
    # *50
    list_container.append(neural_network.learn(test_case).tolist())
    c = list_container[0].pop()
    b = list_container[0].pop()
    a = list_container[0].pop()
    a_percent = abs((a - real_data[0])) / a * 100
    b_percent = abs((b - real_data[1])) / b * 100
    c_percent = abs((c - real_data[2])) / c * 100
    txt_file_name = file_name + ".txt"
    f = open(txt_file_name, "w+")
    str1 = ''.join(str(el) for el in neural_network.synaptic_weights.tolist())
    f.write(str1)
    print(str1)
    f.write("\n" + str(a_percent))
    print(str(a_percent))
    f.write("\n" + str(b_percent))
    print(str(b_percent))
    f.write("\n" + str(c_percent))
    print(str(c_percent))
    f.close()


if __name__ == "__main__":
    file_names = ["normal charge normal discharge_charge_fit", "normal charge normal discharge_discharge_fit",
                  "normal charge overdischarge_charge_fit", "normal charge overdischarge_discharge_fit",
                  "overcharge normal discharge_charge_fit", "overcharge normal discharge_charge_fit",
                  "overcharge overdischarge_charge_fit", "overcharge overdischarge_discharge_fit"]
    for i in range(len(file_names)):
        #file_names[i] = "/Users/xichao/Desktop/fitting data/" + file_names[i] + ".csv"
        csv2txt(file_names[i])
