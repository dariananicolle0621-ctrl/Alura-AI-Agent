def create_retriever(vector_store):
    """
    Convierte la base vectorial en un retriever para realizar búsquedas semánticas.
    """

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )

    return retriever