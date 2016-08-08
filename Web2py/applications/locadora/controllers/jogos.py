# -*- coding: utf-8 -*-

@auth.requires_login()
def gerenciar():
    grid = SQLFORM.grid(Jogos)
    return dict(grid=grid)
