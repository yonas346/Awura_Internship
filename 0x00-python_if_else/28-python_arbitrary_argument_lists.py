#python arbitrary argument lists
def concat(*args, sep="/"):
    return sep.join(args)

concat("yoni", "ermi","nati")