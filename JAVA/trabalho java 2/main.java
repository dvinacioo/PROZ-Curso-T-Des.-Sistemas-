import java.util.Scanner;
import javax.swing.JOptionPane;
public class main 
{
   public static void main(String[] args){

    JOptionPane.showMessageDialog(
        null,
        "Cadastro de Eventos"
    );

    Scanner entrada = new Scanner(System.in);

    // CADASTRANDO EVENTOS
    System.out.println("***** CADASTRE OS EVENTOS ****");
    
    //primeiro evento
    System.out.println("=== EVENTO 1 ===");

    System.out.print("Digite o Código do 1° Evento: ");
    String codigo1 = entrada.nextLine();

    System.out.print("Digite o Nome do 1° Evento: ");
    String nome1 = entrada.nextLine();

    System.out.print("Digite o Local do 1° Evento: ");
    String local1 = entrada.nextLine();

    System.out.print("Digite o Valor de Inscrição do 1° Evento: ");
    double valor1 = entrada.nextDouble();

    System.out.print("Digite o número de Vagas Disponíveis do 1° Evento: ");
    int vagas1 = entrada.nextInt();

    if (vagas1 < 10)
    {
    JOptionPane.showMessageDialog(
        null,
        "Evento com ultimas vagas"
    );      
    }

    System.out.print("Digite quantas Horas vai ter o 1° Evento: ");
    int cargaHoraria1 = entrada.nextInt();
    entrada.nextLine(); // limpa o Enter que ficou pendente
    
    //segundo evento
    System.out.println("=== Evento 2 ===");

    System.out.print("Digite o Código do 2° Evento: ");
    String codigo2 = entrada.nextLine();
    
    System.out.print("Digite o Nome do 2° Evento: ");
    String nome2 = entrada.nextLine();

    System.out.print("Digite o Local do 2° Evento: ");
    String local2 = entrada.nextLine();

    System.out.print("Digite o Valor de Inscrição do 2° Evento: ");
    double valor2 = entrada.nextDouble();

    System.out.print("Digite o número de Vagas Disponíveis do 2° Evento: ");
    int vagas2 = entrada.nextInt();

    if (vagas2 < 10)
    {
    JOptionPane.showMessageDialog(
        null,
        "Evento com ultimas vagas"
    );      
    }

    System.out.print("Digite quantas Horas vai ter o 2° Evento: ");
    int cargaHoraria2 = entrada.nextInt();
     entrada.nextLine(); // limpa o Enter que ficou pendente

    //terceiro evento
    System.out.println("=== Evento 3 ===");

    System.out.print("Digite o Código do 3° Evento: ");
    String codigo3 = entrada.nextLine();

    System.out.print("Digite o Nome do 3° Evento: ");
    String nome3 = entrada.nextLine();

    System.out.print("Digite o Local do 3° Evento: ");
    String local3 = entrada.nextLine();

    System.out.print("Digite o Valor de Inscrição do 3° Evento: ");
    double valor3 = entrada.nextDouble();

    System.out.print("Digite o número de Vagas Disponíveis do 3° Evento: ");
    int vagas3 = entrada.nextInt();

    if (vagas3 < 10)
    {
    JOptionPane.showMessageDialog(
        null,
        "Evento com ultimas vagas"
    );      
    }

    System.out.print("Digite quantas Horas vai ter o 3° Evento: ");
    int cargaHoraria3 = entrada.nextInt();
     entrada.nextLine(); // limpa o Enter que ficou pendente

    eventos evento1 = new eventos(codigo1, nome1, local1, valor1, vagas1, cargaHoraria1);
    eventos evento2 = new eventos(codigo2, nome2, local2, valor2, vagas2, cargaHoraria2);
    eventos evento3 = new eventos(codigo3, nome3, local3, valor3, vagas3, cargaHoraria3);
    

    //exibição dos dados do evento 1
    evento1.mensagemAlerta();
    evento2.mensagemAlerta();
    evento3.mensagemAlerta();

    System.out.println("");
    System.out.println("***** EXIBINDO OS DADOS ******");
    System.out.println("");

    System.out.println("===== Evento 1 =====");
    evento1.exibirDados();
    System.out.println("Nível de vagas: " + evento1.situacaoVagas());
    System.out.println("Tem direito a desconto? " + evento1.permitePromocao());

    System.out.println("");

    System.out.println("===== Evento 2 =====");
    evento2.exibirDados();
    System.out.println("Nível de vagas: " + evento2.situacaoVagas());
    System.out.println("Tem direito a desconto? " + evento2.permitePromocao());

    System.out.println("");

    System.out.println("===== Evento 3 =====");
    evento3.exibirDados();
    System.out.println("Nível de vagas: " + evento3.situacaoVagas());
    System.out.println("Tem direito a desconto? " + evento3.permitePromocao());
}
}