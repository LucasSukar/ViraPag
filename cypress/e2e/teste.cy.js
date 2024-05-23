describe('test suite biblioteca', () => {
    it('Adicionar livro', () => {
        cy.visit('/admin/create-superuser');
        cy.get('input[name="username"]').type('admin');
        cy.get('input[name="email"]').type('admin@example.com');
        cy.get('input[name="password"]').type('admin123');
        cy.get('input[name="confirmPassword"]').type('admin123');
        cy.get('button[type="submit"]').click();
        cy.visit('/');
        cy.get('.nav-link > .logosomb').click()
        cy.get('.btn-primary').click()
        cy.get('.text-primary').click()
        cy.get('#username').type('Joaquim')
        cy.get('#email').type('Joaquim@gmail.com')
        cy.get('#password').type('testando')
        cy.get('.btn').click()
        cy.get('#id_username').type('Joaquim')
        cy.get('#id_password').type('testando')
        cy.get('.btn').click()
        cy.get(':nth-child(3) > a > .bx').click()
        cy.get('.btn').click()
        cy.get('#titulo').type('Guardiola Confidencial')
        cy.get('#autor').type('Marti Perarnau')
        cy.get('#anopublicado').type('2010')
        cy.get('#genero').select('teste 2')
        cy.get('.btn').click()
        cy.get('.list-group-item').click()
        cy.get('.card-title').invoke('text').should('have.string', 'Guardiola Confidencial')
        cy.visit('/admin/');
        cy.get('#id_username').type('admin')
        cy.get('#id_password').type('1234')
        cy.get('.submit-row > input').click()
        cy.get('.model-user > th > a').click()
        cy.get(':nth-child(1) > .action-checkbox > .action-select').click()
        cy.get(':nth-child(2) > .action-checkbox > .action-select').click()
        cy.get('select').select('Delete selected users')
        cy.get('.button').click()
        cy.get('div > [type="submit"]').click()        
    })
})