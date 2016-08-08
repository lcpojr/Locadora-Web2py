# -*- coding: utf-8 -*-

############################################################################
#    NESTE ARQUIVO SERAM DEFINIDOS OS VALIDADORES PARA OS FORMULÁRIOS      #
############################################################################

#############################################################################################
#                        EXEMPLOS DE VALIDADORES                                            #
#   IS_IN_DB:                                                                               #
#      requires = IS_IN_DB(...,multiple=True)                                               #
#   IS_IN_SET:                                                                              #
#      requires = IS_IN_SET(...,multiple=True)                                              #
#   IS_LIST_OF:                                                                             #
#      requires = IS_LIST_OF(...)                                                           #
#   IS_EMAIL:                                                                               #
#      requires = IS_EMAIL(...)                                                             #
#   IS_NOT_EMPTY:                                                                           #
#      requires = IS_NOT_EMPTY(error_message='cannot be empty!')                            #
#   VEJA MAIS EM:                                                                           #
#      http://www.web2py.com/books/default/chapter/29/07/forms-and-validators#Validators    #
#############################################################################################


# Validadores de Clientes
Clientes.nome.requires = IS_NOT_EMPTY()
Clientes.email.requires = IS_EMAIL()


# Validadores de Jogos
Jogos.titulo.requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, Jogos.titulo)]
Jogos.generos.requires = IS_NOT_EMPTY()
Jogos.desenvolvedora.requires = IS_NOT_EMPTY()
Jogos.plataforma.requires = IS_IN_SET(['XBOX 360', 'XBOX ONE', 'PS3', 'PS4', 'Wii', 'Super Nintendo'], zero='Selecione a plataforma', multiple=True)
Jogos.capa.requires = IS_EMPTY_OR(IS_IMAGE())


# Validadores de Estoque
Estoque.jogo.requires = IS_IN_DB(db, Jogos.id, '%(titulo)s', _and = IS_NOT_IN_DB(db, Estoque.jogo))


# Validadores de Locacoes
Locacoes.jogos.requires = IS_IN_DB(db, Jogos.id, '%(titulo)s', multiple=True)
Locacoes.cliente.requires = IS_IN_DB(db, Clientes.id, '%(nome)s')
Locacoes.data_locacao.requires = IS_DATETIME()
Locacoes.data_devolucao.requires = IS_DATETIME()
