typedef char *string;

typedef struct reg celula;
struct reg
{
    int chave, ocorr;
    celula *prox;
};

celula *tb;

unsigned convert_string(string s)
{
    unsigned h = 0;
    for (int i = 0; s[i] != '\0'; i++)
        h = h * 256 + s[i];
    return h;
}

void contabiliza(int ch)
{
    celula *p;
    p = tb;
    while (p != NULL && p->chave != ch)
        p = p->prox;
    if (p != NULL)
        p->ocorr += 1;
    else
    {
        p = new celula;
        p->chave = ch;
        p->ocorr = 1;
        p->prox = tb;
        tb = p;
    }
}
