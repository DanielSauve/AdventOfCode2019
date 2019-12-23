if __name__ == "__main__":
    f = open("day8.txt").read()
    WIDTH, HEIGHT = 25, 6
    NUM_LAYERS = len(f) // (WIDTH * HEIGHT)
    layers = []
    curr = 0
    for _ in range(NUM_LAYERS):
        layers.append([])
        for _ in range(WIDTH * HEIGHT):
            layers[-1].append(f[curr])
            curr += 1

    min_zeros = len(f)
    out = -1
    for layer in layers:
        zeros = layer.count('0')
        if zeros < min_zeros:
            min_zeros = zeros
            out = layer.count('1') * layer.count('2')
    print(out)
    image = []
    for i in range(WIDTH * HEIGHT):
        layer_counter = 0
        curr_layer = layers[layer_counter]
        while curr_layer[i] == '2':
            layer_counter += 1
            curr_layer = layers[layer_counter]
        image.append(curr_layer[i])
    curr_pixel = 0
    for _ in range(HEIGHT):
        for _ in range(WIDTH):
            print("#" if image[curr_pixel] == '1' else ".", end="")
            curr_pixel += 1
        print()
