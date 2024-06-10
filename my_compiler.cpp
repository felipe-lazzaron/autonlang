#include <llvm/IR/IRBuilder.h>
#include <llvm/IR/LLVMContext.h>
#include <llvm/IR/Module.h>
#include <llvm/IR/Verifier.h>
#include <llvm/Support/raw_ostream.h>

using namespace llvm;

LLVMContext Context;
Module *ModuleOb = new Module("my compiler", Context);
IRBuilder<> Builder(Context);

// Função auxiliar para criar variáveis
Value* createVariable(AllocaInst* var, Value* initialValue = nullptr) {
    if (initialValue) {
        Builder.CreateStore(initialValue, var);
    }
    return var;
}

// Função auxiliar para atribuições
void createAssignment(AllocaInst* var, Value* value) {
    Builder.CreateStore(value, var);
}

// Função para criar uma condicional
void createIfCondition(Value* condition, BasicBlock* thenBlock, BasicBlock* elseBlock = nullptr) {
    Builder.CreateCondBr(condition, thenBlock, elseBlock ? elseBlock : thenBlock);
}

// Função para criar um loop
void createWhileLoop(Value* condition, BasicBlock* loopBlock, BasicBlock* afterLoopBlock) {
    Builder.CreateCondBr(condition, loopBlock, afterLoopBlock);
    Builder.SetInsertPoint(loopBlock);
}

// Função principal para gerar LLVM IR
int main() {
    // Exemplo de declaração de variável e atribuição
    FunctionType *mainFuncType = FunctionType::get(Builder.getVoidTy(), false);
    Function *mainFunction = Function::Create(mainFuncType, Function::ExternalLinkage, "main", ModuleOb);
    BasicBlock *entry = BasicBlock::Create(Context, "entry", mainFunction);
    Builder.SetInsertPoint(entry);

    // Declaração de variável 'status'
    AllocaInst *statusVar = Builder.CreateAlloca(Builder.getInt8Ty()->getPointerTo(), nullptr, "status");
    createVariable(statusVar, Builder.CreateGlobalStringPtr("inativo"));

    // Atribuição a 'status'
    createAssignment(statusVar, Builder.CreateGlobalStringPtr("ativo"));

    // Declaração de variável 'velocidade'
    AllocaInst *velocidadeVar = Builder.CreateAlloca(Builder.getInt32Ty(), nullptr, "velocidade");
    createVariable(velocidadeVar, Builder.getInt32(0));

    // Exemplo de condicional
    Value *cond = Builder.CreateICmpSGE(Builder.getInt32(10), Builder.getInt32(0));
    BasicBlock *thenBlock = BasicBlock::Create(Context, "then", mainFunction);
    BasicBlock *elseBlock = BasicBlock::Create(Context, "else", mainFunction);
    createIfCondition(cond, thenBlock, elseBlock);

    // Corpo do 'then'
    Builder.SetInsertPoint(thenBlock);
    createAssignment(velocidadeVar, Builder.getInt32(60));
    Builder.CreateBr(entry);

    // Corpo do 'else'
    Builder.SetInsertPoint(elseBlock);
    createAssignment(velocidadeVar, Builder.getInt32(0));
    Builder.CreateBr(entry);

    // Exemplo de loop 'while'
    BasicBlock *loopBlock = BasicBlock::Create(Context, "loop", mainFunction);
    BasicBlock *afterLoopBlock = BasicBlock::Create(Context, "afterloop", mainFunction);
    createWhileLoop(cond, loopBlock, afterLoopBlock);

    // Corpo do loop
    Builder.SetInsertPoint(loopBlock);
    createAssignment(velocidadeVar, Builder.getInt32(30));
    Builder.CreateBr(entry);

    // Finaliza a função 'main'
    Builder.SetInsertPoint(afterLoopBlock);
    Builder.CreateRetVoid();

    // Verifica a função e imprime o IR
    verifyFunction(*mainFunction);
    ModuleOb->print(outs(), nullptr);

    delete ModuleOb;
    return 0;
}
