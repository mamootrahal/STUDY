import sys
import numpy as np

def log_loss(w, b, X, y, eps=1e-15):
    n = X.shape[0]

    z = X.dot(w) + b
    p = 1 / (1 + np.exp(-z))

    # защита от log(0)
    p = np.clip(p, eps, 1 - eps)

    loss = -(1/n) * np.sum(y * np.log(p) + (1 - y) * np.log(1 - p))

    dw = (1/n) * X.T.dot(p - y)
    db = (1/n) * np.sum(p - y)

    return loss, dw, db


def optimize(w, b, X, y, n_iterations, eta):
    losses = []

    for _ in range(n_iterations):
        loss, dw, db = log_loss(w, b, X, y)

        w = w - eta * dw
        b = b - eta * db

        losses.append(loss)

    return w, b, losses


def predict(w, b, X, p=0.5):
    z = X.dot(w) + b
    probs = 1 / (1 + np.exp(-z))
    y_pred = (probs >= p).astype(int)
    return y_pred


X = np.array([[0], [1]])
y = np.array([0, 1])

w = np.zeros(X.shape[1])
b = 0.0

w, b, _ = optimize(w, b, X, y, n_iterations=5000, eta=0.5)
y_pred = predict(w, b, X)

print(*y_pred)

#exec(sys.stdin.read())
