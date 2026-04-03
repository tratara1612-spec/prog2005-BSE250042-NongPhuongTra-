layers = {
    "layer-11": {
        "layer-21": 90,
        "layer-22": {
            "layer-31": 43
        }
    },
    "layer-12": 35
}

val_12 = layers["layer-12"]
print(f"Giá trị layer-12: {val_12}")
val_31 = layers["layer-11"]["layer-22"]["layer-31"]
print(f"Giá trị layer-31: {val_31}")
