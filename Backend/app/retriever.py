def create_retriever(vector_store):
    """Convierte la base vectorial en un retriever (búsqueda semántica)."""
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )