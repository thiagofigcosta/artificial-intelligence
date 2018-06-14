function [w,b,Err] = perceptron_train(max_it, a, X, D)
    w = 0; b = 0;
    t = 1; E = 1;
    N=size (D)
    N=N(1)
    while t < max_it & E>0 do
        E = 0;
        for i = 1:N
            y(i) = (w*X(i)+b)>=0 //funcao de avaliacao = degrau
            e(i) = D(i) - y(i)
            w = w + a*e(i)*X(i)'
            b = b + a*e(i)
            E = E + e'*e
        end
        Err(t)=E
        t = t+1
    end
endfunction

function [acc] = evaluate(w, b, X, D)
    N=size (D)
    N=N(1)
    acc=0
    for i = 1:N
       y = (w*X(i)+b)>=0 //funcao de avaliacao = degrau
       if(y==D(i)) then
           acc=acc+1
       end
    end
   acc=(acc/N)*100
endfunction
