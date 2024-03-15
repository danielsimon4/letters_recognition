import ... from pytorch

model = SimpleCNN()


# epoch = one complete pass thorught entire df
for epoch in epochs:

    for batch in epoch:

        loss = do_batch()   # Run network forward -> Score  (Should get closer to 0)

        grad = Back_prop() # Run network backwards -> Train (Calculate the gradient of the loss )
        apply(grad)
