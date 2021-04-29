import numpy as np


sigmoid = lambda x: 1 / (1 + np.exp(-x))

def feed_forward(thetas, x):
    a0 = np.vstack((
        np.array([[1]]),
        x
    ))
    z1 = thetas[0] @ a0
    a1 = np.vstack((
        np.array([[1]]),
        sigmoid(z1)
    ))
    z2 = thetas[1] @ a1
    a2 = sigmoid(z2)

    return a2


print(
    feed_forward(
        [
            np.array([
                [0.7, 0.1, 0.3, 0.5],
                [0.8, 0.2, 0.4, 0.6],
            ]),
            np.array([
                [0.9, 1.0, 1.1]
            ])
        ],
        np.array([
            [-0.3],
            [0.08],
            [0.02]
        ])
    )
)

