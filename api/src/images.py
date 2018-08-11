GRAPHS = {
    "bbusers_years.png": {
        "name": "bbusers_years.png",
        "image_url": "http://www.cansolak.com/engr350-project/api/graphs/bbusers_years.png"
    },
    "bbusers_months.png": {
        "name": "bbusers_months.png",
        "image_url": "http://www.cansolak.com/engr350-project/api/graphs/bbusers_months.png"
    }
}


def get_all():
    """
    This function responds to a request for engr350-project/api/graphs
    with the complete lists of graphs

    :return:        sorted list of graphs
    """
    # Create the list of people from our data
    return [GRAPHS[key] for key in sorted(GRAPHS.keys())]


def get_one(graph_name):
    """

    :param graph_name: graph name to be served
    :return: graph
    """
    if graph_name in GRAPHS:
        return GRAPHS.get(graph_name)
    else:
        return None


def create(graph_name, graph_url):
    """

    :param graph_name:
    :param graph_url:
    :return:
    """
    if graph_name not in GRAPHS and graph_name is not None:
        GRAPHS[graph_name] = {"name": graph_url,
                              "image_url": graph_url}
        return "Successful"
    else:
        return None


def update(graph_name, up_graph_name, graph_url):
    """

    :param graph_name:
    :param up_graph_name:
    :param graph_url:
    :return:
    """
    if graph_name not in GRAPHS:
        return None
    else:
        GRAPHS[graph_name] = {"name": up_graph_name,
                              "image_url": graph_url}
        return "Successful"


def delete(graph_name):
    """

    :param graph_name:
    :return:
    """
    if graph_name not in GRAPHS:
        return None
    else:
        del GRAPHS[graph_name]
        return "deleted"

