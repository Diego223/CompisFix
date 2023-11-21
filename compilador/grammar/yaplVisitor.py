# Generated from yapl.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .yaplParser import yaplParser
else:
    from yaplParser import yaplParser

# This class defines a complete generic visitor for a parse tree produced by yaplParser.

class yaplVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by yaplParser#program.
    def visitProgram(self, ctx:yaplParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#classDeclaration.
    def visitClassDeclaration(self, ctx:yaplParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#classBody.
    def visitClassBody(self, ctx:yaplParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#attributeDeclaration.
    def visitAttributeDeclaration(self, ctx:yaplParser.AttributeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#assignmentDeclaration.
    def visitAssignmentDeclaration(self, ctx:yaplParser.AssignmentDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#type.
    def visitType(self, ctx:yaplParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:yaplParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#parameterList.
    def visitParameterList(self, ctx:yaplParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#parameter.
    def visitParameter(self, ctx:yaplParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#statement.
    def visitStatement(self, ctx:yaplParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:yaplParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#letDeclaration.
    def visitLetDeclaration(self, ctx:yaplParser.LetDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#ifStatement.
    def visitIfStatement(self, ctx:yaplParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#whileStatement.
    def visitWhileStatement(self, ctx:yaplParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#methodCallStatement.
    def visitMethodCallStatement(self, ctx:yaplParser.MethodCallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expressionStatement.
    def visitExpressionStatement(self, ctx:yaplParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#returnStatement.
    def visitReturnStatement(self, ctx:yaplParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expressionList.
    def visitExpressionList(self, ctx:yaplParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#block.
    def visitBlock(self, ctx:yaplParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#classMethodCallExpression.
    def visitClassMethodCallExpression(self, ctx:yaplParser.ClassMethodCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#additionExpression.
    def visitAdditionExpression(self, ctx:yaplParser.AdditionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#lessThanOrEqualExpression.
    def visitLessThanOrEqualExpression(self, ctx:yaplParser.LessThanOrEqualExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#newExpression.
    def visitNewExpression(self, ctx:yaplParser.NewExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:yaplParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:yaplParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#notExpression.
    def visitNotExpression(self, ctx:yaplParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#selfLiteralExpression.
    def visitSelfLiteralExpression(self, ctx:yaplParser.SelfLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#multiplicationExpression.
    def visitMultiplicationExpression(self, ctx:yaplParser.MultiplicationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#notEqualExpression.
    def visitNotEqualExpression(self, ctx:yaplParser.NotEqualExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#greaterThanExpression.
    def visitGreaterThanExpression(self, ctx:yaplParser.GreaterThanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#greaterThanOrEqualExpression.
    def visitGreaterThanOrEqualExpression(self, ctx:yaplParser.GreaterThanOrEqualExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#stringLiteralExpression.
    def visitStringLiteralExpression(self, ctx:yaplParser.StringLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#orExpression.
    def visitOrExpression(self, ctx:yaplParser.OrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#unaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx:yaplParser.UnaryMinusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#andExpression.
    def visitAndExpression(self, ctx:yaplParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#trueLiteralExpression.
    def visitTrueLiteralExpression(self, ctx:yaplParser.TrueLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#subtractionExpression.
    def visitSubtractionExpression(self, ctx:yaplParser.SubtractionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#integerLiteralExpression.
    def visitIntegerLiteralExpression(self, ctx:yaplParser.IntegerLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#voidLiteralExpression.
    def visitVoidLiteralExpression(self, ctx:yaplParser.VoidLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#equalityExpression.
    def visitEqualityExpression(self, ctx:yaplParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#lessThanExpression.
    def visitLessThanExpression(self, ctx:yaplParser.LessThanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#divisionExpression.
    def visitDivisionExpression(self, ctx:yaplParser.DivisionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#falseLiteralExpression.
    def visitFalseLiteralExpression(self, ctx:yaplParser.FalseLiteralExpressionContext):
        return self.visitChildren(ctx)



del yaplParser