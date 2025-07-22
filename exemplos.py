from .db import get_cursor

with get_cursor(commit=True) as cur:
    cur.execute(
        """
        INSERT INTO livros (titulo, autor, isbn, preco, estoque)
        VALUES (%s, %s, %s, %s, %s)
        """, (titulo, autor, isbn, preco, estoque)
    )

with get_cursor(commit=True) as cur:
    cur.execute("SELECT estoque FROM livros WHERE isbn = %s FOR UPDATE", (isbn,))
    res = cur.fetchone()
    

with get_cursor(commit=True) as cur:
    cur.execute("UPDATE livros SET estoque = %s WHERE isbn = %s", (novo_estoque, isbn))
