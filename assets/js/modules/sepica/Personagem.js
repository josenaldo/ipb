class Personagem {

    constructor(imagem) {
        this.imagem = imagem;
        this.colunasDoSprite = 4;
        this.linhasDoSprite = 4;
        this.larguraDaImagem = 420;
        this.alturaDaImagem = 504;
        this.matrizSprites = Array();
        this.frameAtual = 0;
        this.alturaDoChao = 120;
        this.deslocamento = 100;

        let indice = 0;
        let x;
        let y;
        for (let i = 0 ; i < this.colunasDoSprite ; i++) {
            for (let j = 0 ; j < this.linhasDoSprite ; j++) {
                indice = this.colunasDoSprite * i + j;

                x = this.larguraDaImagem * j;
                y = this.alturaDaImagem * i;

                this.matrizSprites[indice] = [x, y];
            }
        }

        console.log(this.matrizSprites);

    }

    exibe() {

        // image(img, dx, dy, dWidth, dHeight, sx, sy, [sWidth], [sHeight])
        let dx = this.deslocamento;
        let zoom = 2;
        let tamanhox = this.larguraDaImagem / zoom;
        let tamanhoy = this.alturaDaImagem / zoom;

        let dy = height - tamanhoy - this.alturaDoChao;

        let sx = this.matrizSprites[this.frameAtual][0];
        let sy = this.matrizSprites[this.frameAtual][1];

        image(
            this.imagem,
            dx, dy,
            tamanhox, tamanhoy,
            sx, sy,
            this.larguraDaImagem, this.alturaDaImagem
        );
    }

    anima() {
        this.frameAtual++;

        if(this.frameAtual >= this.matrizSprites.length - 1){
            this.frameAtual = 0;
        }
    }
}