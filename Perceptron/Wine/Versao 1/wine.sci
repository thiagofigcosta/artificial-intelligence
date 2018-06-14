
function [bin]= to_bin(in)
    bin=[0,0,0]
    select in
    case 1 then
        bin=[0,0,1]
    case 2 then
        bin=[0,1,0]
    case 3 then
        bin=[1,0,0]
    end
endfunction

file = read_csv('wine.data')
file = evstr(file)
N=size(file)
N=N(1)
indice=grand(1,"prm",(1:N))

X_train=zeros(ceil(N*0.66),13)
D_train=zeros(ceil(N*0.66),3)
for i = 1:ceil(N*0.66)
    tmp=file(indice(i),:)
    
    for j = 2:14
	    X_train(i,j-1)=tmp(j)
	end
	for j = 1:3
		tmp2=to_bin(tmp(1))
	    D_train(i,j)=tmp2(j)
	end
end

X_test=zeros(ceil(N*0.33),13)
D_test=zeros(ceil(N*0.33),3)
for i = 1:ceil(N*0.33)+1
    tmp=file(indice(i+ceil(N*0.66)),:)
    
    for j = 2:14
	    X_test(i,j-1)=tmp(j)
	end
	for j = 1:3
		tmp2=to_bin(tmp(1))
	    D_test(i,j)=tmp2(j)
	end
end

max_it = 100
taxa_aprendizado = 0.2
[weigths,bias,Err] = perceptron_train(max_it,taxa_aprendizado,X_train,D_train)
taxa_acerto = evaluate(weigths,bias,X_test,D_test)

