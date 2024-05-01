//describe = historia; colocar nome da historia
//it = cenario; colocar numero da historia e do cenario; exemplo (h1c1 -> historia 1 cenario 1)

describe('test suite lista de desejo', () => {
    it('Adicionar livro', () => {
        cy.visit('/');
        cy.get('.nav-link > .logosomb').click()
        cy.get('.btn-primary').click()
        cy.get('#id_username').type('Joaquim')
        cy.get('#id_password').type('testando')
        cy.get('.btn').click()
        cy.get(':nth-child(4) > a > .bx').click()
        cy.get('.btn').click()
        cy.get('#titulo').type('Pequeno principe')
        cy.get('#autor').type('Antoine de Saint-Exupéry')
        cy.get('#anopublicado').type('1943')
        cy.get('.btn').click()
    })
    it('Adicionar outro livro', () => {
        cy.visit('/');
        cy.get('.nav-link > .logosomb').click()
        cy.get('.btn-primary').click()
        cy.get('#id_username').type('Joaquim')
        cy.get('#id_password').type('testando')
        cy.get('.btn').click()
        cy.get(':nth-child(4) > a > .bx').click()
        cy.get('.btn-success').click()
        cy.get('#titulo').type('Romeu e Julieta')
        cy.get('#autor').type('William Shakespear')
        cy.get('#anopublicado').type('1595')
        cy.get('.btn').click()
    })
    it('Mover livro para biblioteca', () => {
        cy.visit('/');
        cy.get('.nav-link > .logosomb').click()
        cy.get('.btn-primary').click()
        cy.get('#id_username').type('Joaquim')
        cy.get('#id_password').type('testando')
        cy.get('.btn').click()
        cy.get(':nth-child(4) > a > .bx').click()
        cy.get('[action="/mainapp/lista_desejos/add_para_colecao/65/"] > .btn').click()
    })
    it('Remover livro da lista de desejo', () => {
        cy.visit('/');
        cy.get('.nav-link > .logosomb').click()
        cy.get('.btn-primary').click()
        cy.get('#id_username').type('Joaquim')
        cy.get('#id_password').type('testando')
        cy.get('.btn').click()
        cy.get(':nth-child(4) > a > .bx').click()
        cy.get('[action="/mainapp/lista_desejos/deletar/66/"] > .btn').click()
    })
  })