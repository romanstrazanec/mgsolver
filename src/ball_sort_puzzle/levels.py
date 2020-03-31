from .color import Color


class Levels:
    l1 = [
        [Color.orange],
        [Color.orange, Color.orange, Color.orange]
    ]

    l2 = [
        [Color.blue, Color.orange, Color.blue, Color.orange],
        [Color.orange, Color.blue, Color.orange, Color.blue],
        []
    ]

    l3 = [
        [Color.blue, Color.orange, Color.red, Color.blue],
        [Color.orange, Color.orange, Color.red, Color.blue],
        [Color.red, Color.blue, Color.orange, Color.red]
    ]
