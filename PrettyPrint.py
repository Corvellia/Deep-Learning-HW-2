def pretty_print(w, eta, iterations, error):
    print(str(w[0]) + " " + str(w[1]) + " " + str(w[2]) + "\n")
    print("CS-5001: HW#2")
    print("Programmer: Albert J Berger")
    print("\nTraining:\nUsing Learning Rate = " + str(eta))
    print("Using " + str(iterations) + " iterations")
    print("\nOutput:\nw0 = " + str(w[0]) + "\nw1 = " + str(w[1]) + "\nw2 = " 
            + str(w[2]))
    print("\nValidation\nSum-of-Squares Error = " + str(error))