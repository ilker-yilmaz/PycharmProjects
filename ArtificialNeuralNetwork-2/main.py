class Network:
    ## Ağırlıklarımızı ve bias değerlerimizi burada oluşturlmaktadır.
    def __init__(self):
        self.weights = [0.0, 0.0, 0.0]
        self.bias = 0.0
    ## Sigmoid fonksiyonu
    def sigmoid(self, x):
        self.x = x
    ## Sigmoid fonksiyonunun türevi
    def sigmoid_turev(self, x):
        self.x = x
    ## İleri beslemeli nöron değerleri hesaplamaları
    def feedforward(self, data):
        self.data = data
    ## Belitiler iteresyon sayısı kadar model eğitimi
    def train(self, data):
        self.data = data

## Ağırlıklarımızı ve bias değerlerimizi burada oluşturulmaktadır.
