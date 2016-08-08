# -*- coding: utf-8 -*-

def locar():
    form = SQLFORM(Locacoes)
    if form.process().accepted:
        session.flash = 'Locação realizada!'
        redirect(URL('locar'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)


def listar():
    locacoes = db(Locacoes).select()
    return dict(locacoes=locacoes)


def alterar():
    form = SQLFORM(Locacoes, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Locação atualizada!'
        redirect(URL('listar'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)


def remover():
    db(Locacoes.id==request.args(0, cast=int)).delete()
    session.flash = 'Locação apagada!'
    redirect(URL('listar'))


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
