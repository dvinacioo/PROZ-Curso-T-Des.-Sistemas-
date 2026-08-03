public class P013_Banco{
    
    public static void main(String[] args){

            ContaBancaria titular1 = new ContaCorrente("Davi", 5000.00, 1540.00);
            ContaBancaria titular2 = new ContaPoupanca("Lucas", 5000.00, 1200.00);
            ContaBancaria titular3 = new CDB("Rafael", 5000.00, 1500.00);

            titular1.calcularRendimento();
            System.out.println();

            titular2.calcularRendimento();
            System.out.println();

            titular3.calcularRendimento();
            System.out.println();
    }
}

// ABSTRAÇÃO
abstract class ContaBancaria {
    // ENCAPSULAMENTO
    private String nome;
    private double saldo;
    private double fatura;

    public ContaBancaria(String nome, double saldo, double fatura) {
        this.nome = nome;
        this.saldo = saldo;
        this.fatura = fatura;
        
    }

    // GETTERS e SETTERS
    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public double getSaldo(){
        return saldo;
    }

    public void setSaldo(double saldo){
        this.saldo = saldo;
    }

    public double getFatura(){
        return fatura;
    }

    public void setFatura(double fatura){
        this.fatura = fatura;
    }

    // METODO ABSTRATO
    public abstract void calcularRendimento();
}

    // HERANÇA
    class ContaCorrente extends ContaBancaria{

        public ContaCorrente(String nome, double saldo, double fatura) {
            super(nome, saldo, fatura);
        }

        // POLIMORFISMO
        @Override
        public void calcularRendimento(){
            double rendimento = getSaldo() * 0.00;

            System.out.println("Conta Corrente");
            System.out.println("Nome: " + getNome());
            System.out.println("Saldo: " + getSaldo());
            System.out.println("Rendimento: " + rendimento);
            System.out.println("Fatura: R$ " + getFatura());
        }
    }

    // HERANÇA
    class ContaPoupanca extends ContaBancaria{

        public ContaPoupanca(String nome, double saldo, double fatura) {
            super(nome, saldo, fatura);
        }

        // POLIMORFISMO
        @Override
        public void calcularRendimento(){
            double rendimento = getSaldo() * 0.019;

            System.out.println("Conta Poupança");
            System.out.println("Nome: " + getNome());
            System.out.println("Saldo: " + getSaldo());
            System.out.println("Rendimento: " + rendimento);
            System.out.println("Fatura: R$ " + getFatura());
        }
    }

        // HERANÇA
    class CDB extends ContaBancaria{

        public CDB(String nome, double saldo, double fatura) {
            super(nome, saldo, fatura);
        }

        // POLIMORFISMO
        @Override
        public void calcularRendimento(){
            double rendimento = getSaldo() * 0.04;

            System.out.println("Rendimento CDB");
            System.out.println("Nome: " + getNome());
            System.out.println("Saldo: " + getSaldo());
            System.out.println("Rendimento: " + rendimento);
            System.out.println("Fatura: R$ " + getFatura());
        }
    }