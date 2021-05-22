import tensorflow as tf
from step7_tensor.model import Model

class Service(object):

    this = Model()

    @tf.function
    def plus(self, num1, num2):
        return tf.add(num1, num2)

    @tf.function
    def minus(self, num1, num2):
        return tf.subtract(num1, num2)

    @tf.function
    def multi(self, num1, num2):
        return tf.multiply(num1, num2)

    @tf.function
    def divid(self, num1, num2):
        return tf.div(num1, num2)
