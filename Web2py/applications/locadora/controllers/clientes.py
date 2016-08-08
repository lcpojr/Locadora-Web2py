# -*- coding: utf-8 -*-

@auth.requires_login()
def gerenciar():
    grid = SQLFORM.grid(Clientes)
    return dict(grid=grid)
