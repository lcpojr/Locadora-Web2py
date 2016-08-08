# -*- coding: utf-8 -*-

######################################################################
#    NESTE ARQUIVO SERAM DEFINIDAS AS TABELAS DO BANCO DE DADOS      #
######################################################################

##############################################################################################################
#   EXEMPLO DE DEFINIÇÃO:                                                                                    #
#        db.define_table('mytable',                                                                          #
#                        Field('myfield','string'))                                                          #
##############################################################################################################

########################################################################
#          PARAMETROS POSSÍVÈIS PARA OS CAMPOS FIELD                   #
#                                                                      #
#    Field(fieldname, type='string', length=None, default=None,        #
#          required=False, requires='<default>',                       #
#          ondelete='CASCADE', notnull=False, unique=False,            #
#          uploadfield=True, widget=None, label=None, comment=None,    #
#          writable=True, readable=True, update=None, authorize=None,  #
#          autodelete=False, represent=None, compute=None,             #
#          uploadfolder=None,                                          #
#          uploadseparate=None,uploadfs=None,                          #
#          rname=None)                                                 #
########################################################################


# Desativando a criação de grupos de usuário
auth.settings.create_user_groups = False


# Criando objeto da tabela de usuário
Usuario = db.auth_user


# Tabela que armazenará os clientes
Clientes = db.define_table('clientes',
    Field('nome', 'string', label='Nome'),
    Field('telefone', 'string', label='Telefone'),
    Field('email', 'string', label='Email')
    )


# Tabela que armazena os jogos
Jogos = db.define_table('jogos',
    Field('titulo', 'string', label='Título'),
    Field('lancamento', 'integer', label='Lançamento'),
    Field('generos', 'list:string', label='Gêneros'),
    Field('plataforma', 'list:string', label='Plaforma'),
    Field('desenvolvedora', 'string', label='Desenvolvedora'),
    Field('capa', 'upload', label='Capa/Cartaz')
    )


# Tabela que armazena os itens em estoque
Estoque = db.define_table('estoque',
    Field('jogo', 'reference jogos', label='Jogo'),
    Field('quantidade', 'integer', label='Quantidade'),
    Field('preco', 'float', label='Preço')
    )


# Tabela que armazena as locações
Locacoes = db.define_table('locacoes',
    Field('jogos', 'list:reference jogos', label='Jogos'),
    Field('cliente', 'reference clientes', label='Cliente'),
    Field('data_locacao', 'datetime', label='Data de Locação'),
    Field('data_devolucao', 'datetime', label='Data de Devolução'),
    Field('multa', 'float', label='Multa')
    )


##############################################################################################################
#                                 EXEMPLOS DE QUERY                                                          #
#   INSERT:                                                                                                  #
#        db.mytable.insert(myfield='value')                                                                  #
#   SELECT:                                                                                                  #
#        rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)                                         #
#   UPDATE:                                                                                                  #
#        db(db.mytable.myfield == 'FIELD').update(myfield='EXEMPLE')                                         #
#   DELETE:                                                                                                  #
#        db(db.mytable.myfield == 'FIELD').delete()                                                          #
#   VEJA MAIS EM:                                                                                            #
#        http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer#Table-constructor  #
##############################################################################################################
