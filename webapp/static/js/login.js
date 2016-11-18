hk = hk || {};

hk.LoginView = BB.View.extend({
    el: '#login',
    loginTemplate: _.template($('#login-template').html()),
    registerTemplate: _.template($('#register-template').html()),

    initialize: function () {
        this.register = false;
        this.render();
    },

    render: function () {
        if (this.register) {
            this.$el.empty().append(this.registerTemplate());
            this.$el.find('.register-wrapper').css({'margin-top': $(window).height()/4});
        } else {
            this.$el.empty().append(this.loginTemplate());
            this.$el.find('.login-wrapper').css({'margin-top': $(window).height()/4});
        }
    },

    events: {
        'click .login-button': 'login',
        'click .register-link': 'swapToRegister',
        'click .login-link': 'swapToLogin',
        'click .register-button': 'register'
    },

    login: function () {
        var username = this.$el.find('#username').val(),
            password = this.$el.find('#password').val();

        if (username && password) {
            $.ajax({
                type: 'POST',
                url: 'auth/login',
                data: {
                    username: username,
                    password: password
                },
                success: function () {
                    window.location.replace('/');
                },
                error: function (data) {
                    if (data.status === 400) {
                        Materialize.toast(data.statusText, 2000);
                    } else if (data.status === 500 && data.statusText == "inactive account") {
                        window.location.replace('/beta');
                    } else {
                        Materialize.toast(data.statusText, 2000);
                    }
                }
            });
        } else {
            Materialize.toast('<span class="subtitle-lato white-text">Please input your username and password</span>', 2000);
        }
    },

    swapToRegister: function () {
        this.register = true;
        this.render();
    },

    swapToLogin: function () {
        this.register = false;
        this.render();
    },

    register: function () {
        var email = this.$el.find('#email').val(),
            username = this.$el.find('#username').val(),
            password = this.$el.find('#password').val();

        if (email && password && username) {

            $.ajax({
                type: 'POST',
                url: 'auth/register',
                data: {
                    email: email,
                    username: username,
                    password: password
                },
                success: function () {
                    window.location.replace('/');
                },
                error: function (data) {
                    if (data.status_code === 400) {
                        Materialize.toast(data.message, 3000);
                    } else if (data.status_code === 500) {
                        Materialize.toast('Internal Server Error', 3000);
                    } else {
                        Materialize.toast(data.statusText, 2000);
                    }
                }
            });

        } else {
            Materialize.toast('<span class="subtitle-lato white-text">Please fill all the fields</span>', 3000);
        }
    }
});
