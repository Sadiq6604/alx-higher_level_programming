#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return (list(map(lambda n: replace if n is search else n,  my_list)))
