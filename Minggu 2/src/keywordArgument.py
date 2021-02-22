def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

    parrot(1000)
    parrot(voltage=1000)
    parrot(voltage=1000000, action='VOOOOOM')
    parrot(action='VOOOOOM', voltage=1000000)
    parrot('a million', 'benefit of life', 'jump')
    parrot('a thounsand', state='pushing up the daisies')

    parrot()
    parrot(voltage=5.0, 'dead')
    parrot(110, voltage=220)
    parrot(actor='John Cleese')

    def function(a):
        pass
    function(0, a=0)