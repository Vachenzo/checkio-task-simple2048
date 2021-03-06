"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ([[0, 2, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 'up'),
            "answer": [[0, 2, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
        },
        {
            "input": ([[0, 2, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]], 'down'),
            "answer": [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 2, 2]]
        },
        {
            "input": ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 2, 2]], 'left'),
            "answer":[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [4, 4, 0, 2]]
        },
        {
            "input": ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [4, 4, 0, 2]], 'right')
            "answer": [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 8, 2]]
        }
    ],
    "Extra": [
        {
            "input": ([[32, 2, 256, 64], [128, 32, 16, 32], [16, 16, 0, 0], [0, 0, 0, 0]], 'up'),
            "answer": [[32, 2, 256, 64], [128, 32, 16, 32], [16, 16, 0, 0], [0, 0, 0, 0]],
            "explanation":"nothing to merge"
        },
        {
            "input": ([[0, 0, 0, 0], [16, 16, 0, 0], [128, 32, 16, 32], [32, 2, 256, 64]], 'down'),
            "answer": [[0, 0, 0, 0], [16, 16, 0, 0], [128, 32, 16, 32], [32, 2, 256, 64]],
            "explanation":"nothing to merge"
        },
        {
            "input": ([[32, 128, 16, 0], [2, 32, 16, 0], [256, 16, 0, 0], [64, 32, 0, 0]], 'left'),
            "answer": [[32, 128, 16, 0], [2, 32, 16, 0], [256, 16, 0, 0], [64, 32, 0, 0]],
            "explanation":"nothing to merge"
        },
        {
            "input": ([[0, 0, 128, 32], [0, 0, 32, 2], [0, 16, 2, 256], [0, 16, 32, 64]], 'right')
            "answer": [[0, 0, 128, 32], [0, 0, 32, 2], [0, 16, 2, 256], [0, 16, 32, 64]],
            "explanation":"nothing to merge"
        }
    ]
}
