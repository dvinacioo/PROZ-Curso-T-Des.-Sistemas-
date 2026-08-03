import javax.swing.JOptionPane;
public class eventos{

    private String codigoEvento;
    private String nomeEvento;
    private String localEvento;
    private double valorInscricao;
    private int vagasDisponiveis;
    private int cargaHoraria;

    public eventos(String codigoEvento, String nomeEvento, String localEvento, double valorInscricao, int vagasDisponiveis, int cargaHoraria){
        this.codigoEvento = codigoEvento;
        this.nomeEvento = nomeEvento;
        this.localEvento = localEvento;
        this.valorInscricao = valorInscricao;
        this.vagasDisponiveis = vagasDisponiveis;
        this.cargaHoraria = cargaHoraria;
    }

    public void exibirDados(){
        System.out.println("Código do Evento: " + codigoEvento);
        System.out.println("Nome do Evento: " + nomeEvento);
        System.out.println("Local do Evento: " + localEvento);
        System.out.println("Valor da Inscrição: " + valorInscricao);
        System.out.println("Vagas Disponíveis: " + vagasDisponiveis);
        System.out.println("Horas de Evento: " + cargaHoraria);
    }

    public boolean vagaDisponível(){
        return vagasDisponiveis > 1;
    }

    public String situacaoVagas(){
        if (vagasDisponiveis <= 10) {
            return "ULTIMAS VAGAS";
        } else if(vagasDisponiveis >= 10 && vagasDisponiveis <= 30){
            return "VAGAS MODERADAS";
        } else{
            return "MUITAS VAGAS DISPONÍVEIS";
        }
    }

    public boolean permitePromocao(){
        return valorInscricao > 300;
    }

    public void mensagemAlerta(){
        if (vagasDisponiveis < 10){
            JOptionPane.showMessageDialog(
        null,
        "ATENÇÃO O EVENTO " + nomeEvento + " ESTÁ COM AS ULTIMAS VAGAS!!!"
    );
        };
    }

}