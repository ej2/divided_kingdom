
BasicGame.Game = function (game) {

};

BasicGame.Game.prototype = {

preload: function () {

    this.load.image('background', '/static/images/game/background.png');
    this.load.image('grass', '/static/images/game/grass.png');
    this.load.image('dirt', '/static/images/game/dirt.png');
    this.load.spritesheet('rock', '/static/images/game/rock.png', 32, 32);
    this.load.spritesheet('snake', '/static/images/game/snake128.png', 128, 128);
    this.load.spritesheet('sam', '/static/images/game/sam.png', 46, 46);
    this.load.spritesheet('knight', '/static/images/game/knight-walk.png', 24, 32);
    this.load.spritesheet('owl2', '/static/images/game/owl01.png', 101, 108);
    this.load.spritesheet('owl', '/static/images/game/owl-knight-walk.png', 70, 76);

    //this.load.spritesheet('boss', '/static/assets/boss.png', 93, 75);
    //this.load.spritesheet('greenEnemy', '/static/assets/enemy.png', 32, 32);

},

create: function () {
    this.setupBackground();
    this.setupPlayer();
    this.setupRocks();
    //this.setupEnemies();
    //this.setupBullets();
    //this.setupExplosions();
    //this.setupPlayerIcons();
    //this.setupText();

    this.cursors = this.input.keyboard.createCursorKeys();
  },

  update: function () {

    //this.snake.x += 1;
    //this.sam.x += 1;

    this.processPlayerInput();
    this.checkCollisions();
    this.rockSpawn();
  },

  render: function() {

    //this.game.debug.body(this.bullet);
   //this.game.debug.body(this.enemy);

  },

setupRocks: function () {
    this.rockPool = this.add.group();
    this.rockPool.enableBody = true;
    this.rockPool.physicsBodyType = Phaser.Physics.ARCADE;
    this.rockPool.createMultiple(10, 'rock');
    this.rockPool.setAll('anchor.x', 0.5);
    this.rockPool.setAll('anchor.y', 0.5);
    this.rockPool.setAll('collideWorldBounds', true);

    // Set the animation for each sprite
    this.rockPool.forEach(function (rock) {
        rock.body.bounce.setTo(1.1, 1.1);
    });

},

rockSpawn: function () {

    if (this.rockPool.countDead() > 0) {

        var rock = this.rockPool.getFirstExists(false);
        // spawn at a random location top of the screen
        rock.reset(this.rnd.integerInRange(20, 780), this.rnd.integerInRange(20, 780));
        // also randomize the speed
        //rock.body.velocity.y = this.rnd.integerInRange(30, 60);
        //rock.body.velocity.x = this.rnd.integerInRange(30, 60);
        rock.body.bounce.setTo(0.8, 0.8);
        rock.body.collideWorldBounds = true;
    }

},

checkCollisions: function () {
    this.physics.arcade.collide(this.player, this.rockPool);
    this.physics.arcade.collide(this.rockPool);

},

processPlayerInput: function () {
    this.player.body.velocity.x = 0;
    this.player.body.velocity.y = 0;

    if (this.cursors.left.isDown) {
    this.player.body.velocity.x = -this.player.speed;
    } else if (this.cursors.right.isDown) {
    this.player.body.velocity.x = this.player.speed;
    }

    if (this.cursors.up.isDown) {
    this.player.body.velocity.y = -this.player.speed;
    } else if (this.cursors.down.isDown) {
    this.player.body.velocity.y = this.player.speed;
    }

    if (this.input.activePointer.isDown &&
    this.physics.arcade.distanceToPointer(this.player) > 15) {
    this.physics.arcade.moveToPointer(this.player, this.player.speed);
    }


    if(5 == 6) {
        if (this.player.body.velocity.x == 0) {

            if (this.player.body.velocity.y < 0) {
                this.player.play("up");
            }
            else {
                this.player.play("down");
            }
        }
        else {

            if (this.player.body.velocity.x > 0) {
                this.player.play('right');
            }
            else {
                this.player.play('left');
            }
        }
    }

},

setupBackground: function () {
    this.ground = this.add.tileSprite(0, 0, this.game.width, this.game.height, 'dirt');
    //this.sea.autoScroll(0, BasicGame.SEA_SCROLL_SPEED);
},

setupText: function () {
    this.instructions = this.add.text( this.game.width / 2, this.game.height - 100,
    'Use Arrow Keys to Move, Press Z to Fire\n' +
    'Tapping/clicking does both',
    { font: '20px monospace', fill: '#fff', align: 'center' }
    );
    this.instructions.anchor.setTo(0.5, 0.5);
    this.instExpire = this.time.now + BasicGame.INSTRUCTION_EXPIRE;

    this.score = 0;
    this.scoreText = this.add.text(
    this.game.width / 2, 30, '' + this.score,
    { font: '20px monospace', fill: '#fff', align: 'center' }
    );
    this.scoreText.anchor.setTo(0.5, 0.5);

},


setupPlayer: function () {
    this.player = this.add.sprite(this.game.width / 2, this.game.height - 50, 'owl');
    this.player.anchor.setTo(0.5, 0.5);

    this.player.animations.add('down', [0, 1, 2], 10, true);
    //this.player.animations.add('up', [3, 4, 5], 10, true);
    //this.player.animations.add('right', [6, 7, 8], 10, true);
    //this.player.animations.add('left', [9, 10, 11], 10, true);
    //this.player.play('left');
    this.player.play('down');

    this.physics.enable(this.player, Phaser.Physics.ARCADE);
    this.player.speed = BasicGame.PLAYER_SPEED;
    this.player.body.collideWorldBounds = true;
    this.player.body.bounce.setTo(1, 1);

    // 20 x 20 pixel hitbox, centered a little bit higher than the center
    this.player.body.setSize(80, 80, 0, -5);
},


  quitGame: function (pointer) {

    //  Here you should destroy anything you no longer need.
    //  Stop music, delete sprites, purge caches, free resources, all that good stuff.

    this.background.destroy();

    // Then let's go back to the main menu.
    this.state.start('MainMenu');


  }

};
